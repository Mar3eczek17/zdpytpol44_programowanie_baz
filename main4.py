from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Silnik
engine = create_engine('sqlite:///chinook.sqlite') # -> Engine
print(engine)
# print(type(engine))
# print(dir(engine))

# Połączenie
connection = engine.connect()  # -> Connectio
print(type(connection))
print(dir(connection))

# Odbicie (dwa obiekty potrzebne)

# 1. Kontener na metadane o odbijanej tabeli
metadata = MetaData()  # -> Metadata
# print(type(metadata))

# 2. Obiekt reprezentujący odbitą tabelę
invoice = Table('invoices', metadata, autoload=True, autoload_with=engine)  # -> Table
print(invoice)
print(type(invoice))
print(dir(invoice))

# Wyświetlmy kolumny
columns = invoice.columns # -> ImmutableColumnCollection
print(columns)
print(type(columns))
print(dir(columns))

# Do elementów ImmutableColumnCollection możemy odwoływać
# na trzy sposoby
# Wyświetlmy pierwszą kolumnę
# Dostęp poprzez indeks (jak lista)
first_column = columns['InvoiceId']  # -> klassy obiekt
print(first_column)
# Dostęp poprzez klucz (jak słownik)
first_column = columns.InvoiceId
# Dostęp poprzez atrybut
first_column = columns.InvoiceId
print(first_column)

# Popatrzmy na pojedynczą kolumnę
print(type(first_column))
print(dir(first_column))

# Typ kolumn
print(first_column.type)

# A co jeżeli chcemy wyświetlić informację o wszystkich kolumnach?
print(repr(invoice))

# I możemy tak
print(metadata.tables)

# Zapytania
# SELECT
stmt = select([invoice])  # -> Select
print(stmt)
print(type(stmt))
print(dir(stmt))

# Obiekt zapytania
result_proxy = connection.execute(stmt)  # -> LegancyCursorResult
print(type(result_proxy))
print(dir(result_proxy))

results = result_proxy.fetchall()  # -> List
print(results)
print(type(results))

first_row = results[0]  # -> LegacyRow
print(first_row)
print(type(first_row))
print(dir(first_row))
print(first_row.keys())
# Mamy trzy metody dostępu ?
# 1. po indeksie
print(first_row[0])
# 2. po kluczu
print(first_row['InvoiceId'])
# 3. po atrybucie
print(first_row.InvoiceId)