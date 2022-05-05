#!/usr/bin/env python3

# Logical implementaion
# 1) create a payload
#
# 2) request the keywords
#    

import faust
import json
from typing import List

from config import KafkaConfig, Parameters, Fields
from helper_functions import log, logger


class TrendsData(faust.Record, serializer=Fields.JSON):
    data = List[str]


app = faust.App(
    KafkaConfig.GROUP_ID,
    broker=KafkaConfig.KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=Fields.RAW

)

data_topic = app.topic(KafkaConfig.TOPIC)

@app.agent(data_topic)
@log
async def fetch_data(raw_data: TrendsData) -> None:
    async for data in raw_data:
        # push the data to google cloud storage
        # data = json.loads(data)
        logger.debug("data fetched from the kafka stream is..")
        data = data.decode("utf-8")
        logger.debug(len(data))
        logger.debug(data)

if __name__ == "__main__":
    app.main()