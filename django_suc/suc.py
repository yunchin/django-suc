from typing import Type

from django.apps import AppConfig
from django.db import connection
from django.db.models import Model, UniqueConstraint
from django.db.models.signals import class_prepared

TEMP_NAME = 'TEMP_NAME'


class SmartUniqueConstraint(UniqueConstraint):
    '''
    This class does exactly what UniqueConstraint does except setting a default value (None) to name, sparing the developer from assigning it manually
    '''
    def __init__(self, name=None, *args, **kwargs):
        # name must be a non-blank string for UniqueConstraint obj's initialization to work
        name = name or TEMP_NAME
        super().__init__(*args, **kwargs, name=name)


class SmartAppConfig(AppConfig):
    '''
    Set unique constraints' name when preparing class with signal
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_prepared.connect(setup_unique_constraints)


def setup_unique_constraints(sender, **kwargs):
    if meta := getattr(sender, '_meta', None):
        for con in getattr(meta, 'constraints', []):
            update_constraint_name(sender, con)


def update_constraint_name(model: Type[Model], constraint: UniqueConstraint) -> None:
    # If the name is assigned manually, use it
    if constraint.name != TEMP_NAME:
        return
    
    # Otherwise, assign a unique name to this constraint
    fields = constraint.fields
    with connection.schema_editor() as editor:
        name = editor._create_index_name(model._meta.db_table, fields, '_uniq')
    constraint.name = name
