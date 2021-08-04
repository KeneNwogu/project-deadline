# project-deadline

## Returns JSON formatted responses that gives information about a Project's deadline

### Params
** Accepts only GET requests **
1. start-date (required) - Specifies the project's start date
2. deadline (required) - Specifies the time allocated to the project
3. time-format (optional, default: "weeks") - Specifies the time format for the deadline period (weeks or months)

### Response

Returns a json of the format 
1. time-format=months

`{
        "deadline": deadline + time_format,
        'estimated-deadline-date': month/day/year,
        "months-left": integer,
        "weeks-left": integer,
        "days-left": integer
 }   
`
2. time-format=weeks
`{
        "deadline": deadline + time_format,
        'estimated-deadline-date': month/day/year,
        "weeks-left": integer,
        "days-left": integer
}   
`
3. If Deadline has passed
`{
     "info": "Deadline has been exhausted",
     "relative": "{integer} weeks/months ago"
 }  
`

4. If start-date has not been reached
`{
     "info": "Project start date has not been reached",
     "estimated_start_date":f"month/day/year",
     "hours-to-start": f"{integer} hours"
 } 
`
