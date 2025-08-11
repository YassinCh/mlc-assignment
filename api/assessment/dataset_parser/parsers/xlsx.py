from io import BytesIO
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset.model import Dataset


class XlsxParser:

    def __init__(self, session: AsyncSession, dataset: Dataset):
        self.session = session
        self.dataset = dataset

    async def parse(self, bytes: BytesIO):
        # TODO: Maak van een bytesIO object een Excel file en parse deze naar een Dataset object.
        # Hints:
        # - De `self.session: AsyncSession` is al een instantie van een SqlAlchemy sessie, deze hoef je dus niet opnieuw te maken.
        # - Maak gebruik van OpenPyXL om de Excel file te openen (https://openpyxl.readthedocs.io/en/stable/tutorial.html)
        # - Kijk naar de documentatie van SqlAlchemy (https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
        # - Wij maken gebruik van AsyncIO dus je moet de async variant van SqlAlchemy gebruiken (https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-orm)
        raise NotImplementedError()
