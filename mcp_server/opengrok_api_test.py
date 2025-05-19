# Copyright (c) 2025 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import pdb
from ArPyOAuth2 import retryHttpSession

USER_AGENT = "file-app/1.0"

OPENGROK_URL = 'https://opengrok.infra.corp.arista.io/source'
OPENGROK_BETA_URL = 'http://go/opengrokbeta'
OPENGROK_SEARCH_ENDPOINT = "/api/v1/search"

params = {
      "full": "TrafficPolicyTest",
      "def": "",
      "symbol": "",
      "path": "",
      "projects": "eos-trunk",
      "maxresults": "2",
}

jsonUrl = OPENGROK_URL + OPENGROK_SEARCH_ENDPOINT

with retryHttpSession( retries=3 ) as session:
   try:
      request = session.get( url=jsonUrl, params=params )
   except Exception as e:
      raise e
   else:
      print( request.json() )
