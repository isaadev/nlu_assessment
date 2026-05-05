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
            "DATE": string,
            "CODE": string,
            "DESCRIPTION": string,
            "INSPECTOR_COMMENTS": string,
            "STATUS": string
        }   
    ]
        

}

**Response Code:** 404 Not found
**Response Payload:** 
{
    "error": string    
}


## Second endpoint

**Request URL:** /property/<address>/comments/
**Request Method:** POST 
**Request Payload:** 
{
    "author": string,
    "comment": string
}

**Response Code:** 404 Not found
**Response Payload:** 
{
    "error": string    
}

**Response Code:** 201 Created
**Response Payload:**
{
    "message": string
}

## Third endpoint
**Request URL:** /property/scofflaws/violations?since=<yyyy-mm-dd>/
**Request Method:** GET
**Request Payload:** None

**Response Code:** 400
**Response Payload:**
{
    "error": string
}

**Response Code:** 200 OK
**Response Payload:**
[
    string,
    string,
    ...
]


