from sqlalchemy.types import TypeDecorator, String, VARCHAR
from decimal import Decimal


class Currency(TypeDecorator):
    impl = String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(VARCHAR(100))

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return Decimal(value)
