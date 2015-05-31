#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'

"""Initial Geo schema

Revision ID: 00000000000
Revises: None
Create Date: 2015-05-26 14:30:00

"""

# revision identifiers, used by Alembic
revision = '00000000000'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
from lbgeo.model import estados
from lbgeo.model import Base
import logging

log = logging.getLogger()

def upgrade():
    # Check if extension exists
    connection = op.get_bind()

    result = connection.execute("""
    SELECT extname
    FROM pg_extension
    WHERE extname = 'postgis'
    """)

    if len(result.fetchall()) == 0:
        # Try to create extension
        op.execute("CREATE EXTENSION postgis")

    # Now create data model
    Base.metadata.create_all(connection)

    pass


def downgrade():
    pass
