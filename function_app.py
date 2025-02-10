import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.timer_trigger(schedule="*/10 * * * * *", 
              arg_name="mytimer",
              run_on_startup=False) 
def mytimer(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    #commenting to check if deploys are successful