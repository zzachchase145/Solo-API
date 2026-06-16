# ======================================================================================================
# IMPORTS
# =====================================================================================================

from pydantic import BaseModel
from datetime import datetime

# ====================================================================================================
# CUSTOMER COMPLAINT HOTEL POST PYDANTIC MODELS
# ===================================================================================================

# This is where we will validate all our fields for the moment we will allow them to all accept None for testing purposes.

class CreateHotelCustomerComplaint(BaseModel):
    id: int
    caller_number: str | None = None
    caller_name: str | None = None
    complaint_reason: str | None = None
    notes: str | None = None
    stay_date: str | None = None
    call_time: str | None = None
    
                        