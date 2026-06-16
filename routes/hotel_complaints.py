# =====================================================================================================
# IMPORTS
# =====================================================================================================







# getting a basic get route to get my server running

@app.get('/')
async def root():
    print('server is working!')


@app.post('/customer_complaints')

def recieve_customer_complaint():
    
