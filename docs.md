# API Docs


## First endpoint

**Request URL:** /property/<address>/
**Request Method:** GET
**Request Payload:** None

**Response Code:** 200 OK
**Response Payload:** 
{
   "LAST_VIOLATION_DATE": string,
    "SCOFFLAW": boolean,
    "TOTAL_VIOLATION_COUNT": int,
    "VIOLATIONS": [
        {
            DATE: string,
            CODE: string,
            DESCRIPTION: string,
            INSPECTOR_COMMENTS: string,
            STATUS: string
        }   
    ]
        

}

**Response Code:** 404 Not found
**Response Payload:** 
{
    "error": string    
}



