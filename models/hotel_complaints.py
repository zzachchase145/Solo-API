# ======================================================================================================
# IMPORTS
# =====================================================================================================

from pydantic import BaseModel
from datetime import datetime

# ====================================================================================================
# CUSTOMER COMPLAINT HOTEL POST PYDANTIC MODELS
# ===================================================================================================

class CreateHotelCustomerComplaint(BaseModel):
    id: int
    caller_number: str | None = None
    caller_name: str | None = None
    