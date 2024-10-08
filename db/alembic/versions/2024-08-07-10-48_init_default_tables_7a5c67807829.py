"""init_default_tables

Revision ID: 7a5c67807829
Revises: 109d2964dfd
Create Date: 2024-08-07 23:05:27.205806

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7a5c67807829"
down_revision = "109d2964dfd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "food_category",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            comment="Идентификатор категории блюда",
        ),
        sa.Column("name", sa.String(), nullable=True, comment="Наименование категории"),
        sa.Column(
            "is_publish",
            sa.Boolean(),
            nullable=True,
            comment="Опубликованность категории",
        ),
        sa.PrimaryKeyConstraint("id"),
        comment="Категория блюда",
    )
    op.create_table(
        "topping",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            comment="Идентификатор ингредиента",
        ),
        sa.Column(
            "name", sa.String(), nullable=True, comment="Наименование ингредиента"
        ),
        sa.PrimaryKeyConstraint("id"),
        comment="Ингредиент",
    )
    op.create_table(
        "food",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            comment="Идентификатор блюда",
        ),
        sa.Column("name", sa.String(), nullable=True, comment="Наименование блюда"),
        sa.Column("description", sa.Text(), nullable=True, comment="Описание блюда"),
        sa.Column("price", sa.Integer(), nullable=True, comment="Стоимость блюда"),
        sa.Column(
            "is_special", sa.Boolean(), nullable=True, comment="Особенность блюда"
        ),
        sa.Column("is_vegan", sa.Boolean(), nullable=True, comment="Веганское блюдо"),
        sa.Column(
            "is_publish", sa.Boolean(), nullable=True, comment="Опубликованность блюда"
        ),
        sa.Column(
            "category_id",
            sa.Integer(),
            nullable=True,
            comment="Идентификатор категории блюда",
        ),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["food_category.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        comment="Блюдо",
    )
    op.create_table(
        "topping_food_reference",
        sa.Column(
            "food_id", sa.Integer(), nullable=False, comment="Идентификатор блюда"
        ),
        sa.Column(
            "topping_id",
            sa.Integer(),
            nullable=False,
            comment="Идентификатор ингредиента",
        ),
        sa.ForeignKeyConstraint(["food_id"], ["food.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["topping_id"], ["topping.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("food_id", "topping_id"),
        comment="Таблица m2m для связи ингредиентов и блюд",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("topping_food_reference")
    op.drop_table("food")
    op.drop_table("topping")
    op.drop_table("food_category")
    # ### end Alembic commands ###
