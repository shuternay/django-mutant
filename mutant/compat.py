from operator import attrgetter
from typing import Iterable, Tuple

import django
from django.db.migrations.state import ModelState
from django.db.models.fields import Field

get_remote_field = attrgetter('remote_field')


def get_remote_field_model(field):
    model = getattr(field, 'model', None)
    if model:
        return field.remote_field.model
    else:
        return field.related_model


def get_opts_label(opts):
    return opts.label


def many_to_many_set(instance, m2m, value):
    getattr(instance, m2m).set(value)


if django.VERSION >= (3, 1):
    def get_model_state_fields_list(model_state: ModelState) -> Iterable[Tuple[str, Field]]:
        return model_state.fields.items()
else:
    def get_model_state_fields_list(model_state: ModelState) -> Iterable[Tuple[str, Field]]:
        return model_state.fields
