# =====================================================================================================
# IMPORTS
# =====================================================================================================

from fastapi import FastAPI
from main import app


# ==========================================================================================================
# CUSTOMER STAY COMPLAINT HOTEL
# =========================================================================================================

# getting a basic get route to get my server running

@app.post('/hotel-complaints')

def create_hotel_complaint():
    
    return {
        'id': app.get('id'),
        'caller_number': app.get('caller_number'),
        'caller_name': app.get('caller_name')
    }