HackerOne API v1 NAV

Shell Python Ruby Java Javascript Go

# Customer Resources

## Activities

### Get Activity

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/activities/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/activities/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/activities/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/activities/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/activities/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/activities/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

activity found

```
{
  "data": {
    "id": "1337",
    "type": "activity-comment",
    "attributes": {
      "message": "Comment!",
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "internal": false
    },
    "relationships": {
      "actor": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "attachments": {
        "data": [
          {
            "id": "1337",
            "type": "attachment",
            "attributes": {
              "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
              "created_at": "2016-02-02T04:05:06.000Z",
              "file_name": "root.rb",
              "content_type": "text/x-ruby",
              "file_size": 2871
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-05-23

`GET /activities/{id}`

An activity object can be fetched by sending a GET request to a unique activity object. In case the request was successful, the API will respond with an [activity object](https://api.hackerone.com/customer-reference#activity).

The included activity relationships depend on the type of activity that is returned. See the [activity object](https://api.hackerone.com/customer-reference#activity) for possible types and relationships.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the activity. |

### Query Activities

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/incremental/activities?handle=string" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/incremental/activities',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  params={
      'handle': 'string'
  },
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/incremental/activities',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/incremental/activities?handle=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/incremental/activities?handle=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/incremental/activities", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

programs found

```
{
  "data": [
    {
      "type": "activity-bug-filed",
      "id": "1337",
      "attributes": {
        "report_id": "99900",
        "message": "",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2017-02-02T04:05:06.000Z",
        "internal": false
      },
      "relationships": {
        "actor": {
          "data": {
            "type": "user",
            "id": "7331",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        }
      }
    }
  ],
  "meta": {
    "max_updated_at": "2017-02-02T04:05:06.000Z"
  },
  "links": {
    "self": "https://api.hackerone.com/v1/incremental/activities?handle=acme&page%5Bsize%5D=1",
    "next": "https://api.hackerone.com/v1/incremental/activities?handle=acme&page%5Bsize%5D=1&page%5Bnumber%5D=2",
    "last": "https://api.hackerone.com/v1/incremental/activities?handle=acme&page%5Bsize%5D=1&page%5Bnumber%5D=20"
  }
}

```

Last revised: 2025-05-23

`GET /incremental/activities`

This endpoint allows you to fetch all activities of your program incrementally by time.

This endpoint is used to:

- Detect a new report or a new activity on a report using a single endpoint.
- Be able to take actions on reports based on user activity. For example, automatically assigning a report after triaging.
- Monitor activities on a program.

The next section will give an overview of what an Activity object looks like. The sections after that will show the endpoints that have been implemented for this resource.

Note: The request URL path is /incremental/activities. When the request is successful, the API will respond with paginated [activity objects](https://api.hackerone.com/customer-reference#activity) ordered by updated date.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| handle | query | string | true | The HackerOne handle of the program with activities you wish to retrieve. |
| report_id | query | integer | false | The ID of the report you wish to retrieve activities for. |
| updated_at_after | query | string | false | A datetime encoded as a string. Used to indicate what cut-off date to use when retrieving activities. When not provided, no filtering is applied and all activities will be retrieved. |
| sort | query | any | false | The attributes to sort the activities on. |
| order | query | any | false | The direction to sort the activities on, by default desc. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

Detailed descriptions

sort: The attributes to sort the activities on.

This parameter may contain multiple attributes that the activities should be sorted on. Sorting is applied in the specified order of attributes, by default descending.

The following attributes can be used for sorting: report_id, created_at, updated_at.

order: The direction to sort the activities on, by default desc.

The following attributes can be used for sorting: asc (ascending), desc (descending).

## Analytics

### Get Analytics Data

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/analytics?key=string&interval=string&start_at=string&end_at=string&organization_id=string" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/analytics',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  params={
      'key': 'string',  'interval': 'string',  'start_at': 'string',  'end_at': 'string',  'organization_id': 'string'
  },
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/analytics',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/analytics?key=string&interval=string&start_at=string&end_at=string&organization_id=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/analytics?key=string&interval=string&start_at=string&end_at=string&organization_id=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/analytics", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

data found with valid params

```
[
  {
    "keys": [
      "report_count",
      "interval"
    ],
    "values": [
      [
        "10",
        "2022-01-01 00:00:00 UTC"
      ],
      [
        "27",
        "2022-04-01 00:00:00 UTC"
      ],
      [
        "35",
        "2022-07-01 00:00:00 UTC"
      ]
    ]
  }
]

```

Last revised: 2026-04-13

`GET /analytics`

This endpoint returns data for a specified`key` corresponding to a predefined analytics query. Values for`key` are derived from the names of charts on these dashboards:

Submissions

- submission-signal
- submissions-benchmarks
- submissions-by-asset
- submissions-by-duplicates
- submissions-by-number-of-collaborators
- submissions-by-severity
- submissions-by-weakness
- submissions-prior-year
- submissions
- top-weaknesses-by-submission-count

Rewards

- bounty-awarded
- bounty-by-asset
- bounty-by-severity
- bounty-by-weakness
- median-reward-benchmarks
- median-reward-prior-year
- median-reward
- rewards-prior-year

Hacker engagement

- active-hackers-prior-year
- active-hackers
- hacker-participation-prior-year
- hacker-participation
- invitation-funnel
- new-hackers-vs-submissions
- returning-hackers-vs-submissions
- top-hackers-severity
- top-hackers-submissions
- top-hackers-total-bounties

Statistics

- closed_submissions_statistics
- disclosure_statistics
- invitations_statistics
- resolution_statistics
- retests_statistics
- reward_statistics
- sla_statistics
- submissions_statistics
- triage_statistics

Response efficiency

- response_efficiency
- response_efficiency_benchmarks
- response_efficiency_missed_standards
- response_efficiency_missed_target
- response_efficiency_on_target
- response_efficiency_top_metrics

Mediations

- filed_mediations
- mediations_by_party
- mediations_by_state
- mediations_by_type
- open_mediations
- top_requesters

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| key | query | string | true | Filter by the query key you want to fetch data for |
| interval | query | string | true | The interval to use for the input date range. Valid intervals are`month`,`quarter`, or`year` |
| start_at | query | string | true | The start date of the query as a string, inclusive. Format YYYY-MM-DD |
| end_at | query | string | true | The end date of the query as a string, exclusive. Format YYYY-MM-DD |
| team_id | query | string | false | Filter by a team/program ID. If no team_id is provided, then data will be for all teams/programs in the organization |
| organization_id | query | string | true | Filter by an organization ID |

## Credentials

### Get Credentials

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials?program_id=0&structured_scope_id=0" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/credentials',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  params={
      'program_id': '0',  'structured_scope_id': '0'
  },
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/credentials',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials?program_id=0&structured_scope_id=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials?program_id=0&structured_scope_id=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/credentials", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

data found with valid params

```
{
  "data": [
    {
      "id": "1",
      "type": "credential",
      "attributes": {
        "credentials": {
          "table": {
            "username": "test",
            "password": "d282032e02b3d1d956ae1a9dea945535"
          }
        },
        "revoked": false,
        "account_details": "test_account_details"
      }
    },
    {
      "id": "2",
      "type": "credential",
      "attributes": {
        "credentials": {
          "table": {
            "username": "test",
            "password": "28cf5ecddb0d781a06beed30f69a5afe"
          }
        },
        "revoked": false,
        "account_details": "test_account_details"
      }
    },
    {
      "id": "3",
      "type": "credential",
      "attributes": {
        "credentials": {
          "table": {
            "username": "test",
            "password": "643c17a23d2fb7f5dd3e17e94cb47d64"
          }
        },
        "revoked": false,
        "account_details": "test_account_details"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /credentials`

Credentials can be fetched for a structured scope by sending a GET request to the credentials endpoint. When the request is successful, the API will respond with paginated [credentials objects](https://api.hackerone.com/customer-reference/#credential).

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | query | integer | true | The ID of the program. You can find the ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| structured_scope_id | query | integer | true | The ID of the structured scope. You can find the structured scope ID by [fetching your programs structured scopes](https://api.hackerone.com/customer-resources#programs-get-structured-scopes). |
| state | query | string | false | An optional state to filter your credentials. It can be`revoked`,`available` or`claimed` |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create a Credential

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "structured_scope_id": 0,
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "{\"username\":\"username1\",\"password\":\"example passowrd\",\"admin_username\":\"admin_user_1\",\"admin_password\":\"admin_pass_1\"}",
      "assignee": "hacker_username"
    }
  },
  "batch_id": "string"
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "structured_scope_id": 0,
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "{\"username\":\"username1\",\"password\":\"example passowrd\",\"admin_username\":\"admin_user_1\",\"admin_password\":\"admin_pass_1\"}",
      "assignee": "hacker_username"
    }
  },
  "batch_id": "string"
}

r = requests.post(
  'https://api.hackerone.com/v1/credentials',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "structured_scope_id": 0,
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "{\"username\":\"username1\",\"password\":\"example passowrd\",\"admin_username\":\"admin_user_1\",\"admin_password\":\"admin_pass_1\"}",
      "assignee": "hacker_username"
    }
  },
  "batch_id": "string"
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/credentials',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"{\\\"username\\\":\\\"username1\\\",\\\"password\\\":\\\"example passowrd\\\",\\\"admin_username\\\":\\\"admin_user_1\\\",\\\"admin_password\\\":\\\"admin_pass_1\\\"}\",\n      \"assignee\": \"hacker_username\"\n    }\n  },\n  \"batch_id\": \"string\"\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"{\\\"username\\\":\\\"username1\\\",\\\"password\\\":\\\"example passowrd\\\",\\\"admin_username\\\":\\\"admin_user_1\\\",\\\"admin_password\\\":\\\"admin_pass_1\\\"}\",\n      \"assignee\": \"hacker_username\"\n    }\n  },\n  \"batch_id\": \"string\"\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"{\\\"username\\\":\\\"username1\\\",\\\"password\\\":\\\"example passowrd\\\",\\\"admin_username\\\":\\\"admin_user_1\\\",\\\"admin_password\\\":\\\"admin_pass_1\\\"}\",\n      \"assignee\": \"hacker_username\"\n    }\n  },\n  \"batch_id\": \"string\"\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/credentials", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential created

```
{
  "data": {
    "id": "<id>",
    "type": "credential",
    "attributes": {
      "credentials": {
        "table": {
          "username": "test",
          "password": "test"
        }
      },
      "revoked": false,
      "assignee_id": "<id>",
      "assignee_username": "john_doe_1234"
    }
  }
}

```

Last revised: 2025-05-23

`POST /credentials`

This API endpoint can be used to create new credential. When the API call is successful, a [credential object](https://api.hackerone.com/customer-reference#credential) will be returned. The IDs of a program's structured scopes can be retrieved from programs/{id}/structured_scopes endpoint.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| structured_scope_id | body | integer | true | The ID of the structured scope to which the credential will belong |
| data | body | object | true | The information to create a credential. |
| » type | body | string | true | credential |
| » attributes | body | object | true | none |
| »» credentials | body | string | true | A JSON-encoded hash of credentials that will eventually be provided to the hacker |
| »» assignee | body | string | false | If provided, the credential will be assigned to the specified user |
| batch_id | body | string | false | If provided, the batch will be stored on the credential |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | credential |

### Update a Credential

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "string",
      "recycle": false
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "string",
      "recycle": false
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/credentials/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "credential",
    "attributes": {
      "credentials": "string",
      "recycle": false
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/credentials/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"string\",\n      \"recycle\": false\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"string\",\n      \"recycle\": false\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"credential\",\n    \"attributes\": {\n      \"credentials\": \"string\",\n      \"recycle\": false\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/credentials/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential updated

```
{
  "data": {
    "id": "<id>",
    "type": "credential",
    "attributes": {
      "credentials": {
        "table": {
          "username": "test",
          "password": "test"
        }
      },
      "revoked": false,
      "assignee_id": "<id>",
      "assignee_username": "john_doe_1234"
    }
  }
}

```

Last revised: 2025-05-23

`PUT /credentials/{id}`

This API endpoint can be used to update an existing credential. When the API call is successful, a [credential object](https://api.hackerone.com/customer-reference#credential) will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the credential. |
| data | body | object | true | The information to update a credential. |
| » type | body | string | true | credential |
| » attributes | body | object | true | none |
| »» credentials | body | string | true | A JSON-encoded hash of credentials that will eventually be provided to the hacker |
| »» recycle | body | boolean | false | If true, the assignee will be removed. The default is`false`. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | credential |

### Assign a Credential

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials/{id}/assign" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "username": "string"
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "username": "string"
}

r = requests.put(
  'https://api.hackerone.com/v1/credentials/{id}/assign',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "username": "string"
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/credentials/{id}/assign',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials/{id}/assign");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"username\": \"string\"\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"username\": \"string\"\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials/{id}/assign',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"username\": \"string\"\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/credentials/{id}/assign", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential assigned

```
{
  "data": {
    "id": "<id>",
    "type": "credential",
    "attributes": {
      "credentials": {
        "table": {
          "username": "test",
          "password": "test"
        }
      },
      "revoked": false,
      "assignee_id": "<id>",
      "assignee_username": "john_doe_1234"
    }
  }
}

```

Last revised: 2025-05-23

`PUT /credentials/{id}/assign`

This API endpoint can be used to assign an existing credential. When the API call is successful, a [credential object](https://api.hackerone.com/customer-reference#credential) will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the credential. |
| username | body | string | true | The username of the user to be assigned the credential. |

### Delete a Credential

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials/{id}/" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/credentials/{id}/',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/credentials/{id}/',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials/{id}/',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/credentials/{id}/", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Credential successfully removed

```
{
  "data": {
    "success": true,
    "message": "Credential successfully removed"
  }
}

```

Last revised: 2025-05-23

`DELETE /credentials/{id}/`

This API endpoint can be used to delete an existing credential. When the API call is successful, a success message will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the credential. |

### Revoke a Credential

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/credentials/{id}/revoke" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put(
  'https://api.hackerone.com/v1/credentials/{id}/revoke',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/credentials/{id}/revoke',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/credentials/{id}/revoke");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/credentials/{id}/revoke',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/credentials/{id}/revoke", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential revoked

```
{
  "data": {
    "id": "<id>",
    "type": "credential",
    "attributes": {
      "credentials": {
        "table": {
          "username": "test",
          "password": "test"
        }
      },
      "revoked": true,
      "assignee_id": "<id>",
      "assignee_username": "john_doe_1234"
    }
  }
}

```

Last revised: 2025-05-23

`PUT /credentials/{id}/revoke`

This API endpoint can be used to revoke an existing credential. When the API call is successful, a [credential object](https://api.hackerone.com/customer-reference#credential) will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the credential. |

### Get Credential Inquiry Responses

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

data found with valid params

```
{
  "data": [
    {
      "id": "1337",
      "type": "credential_inquiry_response",
      "attributes": {
        "details": "this is a credential inquiry response",
        "created_at": "2017-01-01T00:00:00.000Z",
        "user": {
          "id": "1",
          "username": "user1"
        }
      }
    },
    {
      "id": "1339",
      "type": "credential_inquiry_response",
      "attributes": {
        "details": "this is a credential inquiry response",
        "created_at": "2017-01-01T00:00:00.000Z",
        "user": {
          "id": "2",
          "username": "user2"
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses`

Credential inquiry responses can be fetched by sending a GET request to the credential inquiry responses endpoint. When the request is successful, the API will respond with paginated [credential inquiry objects](https://api.hackerone.com/customer-customer-reference#credential_inquiry_responses).

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| credential_inquiry_id | path | integer | true | The ID of the credential inquiry. You can find the credential inquiry ID by [fetching your credential inquiries](https://api.hackerone.com/customer-resources#credentials-get-credential-inquiries). |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Delete Credential Inquiry Response

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Credential Inquiry Response successfully removed

```
{
  "data": {
    "success": true,
    "message": "Credential Inquiry Response successfully removed"
  }
}

```

Last revised: 2025-05-23

`DELETE /programs/{program_id}/credential_inquiries/{credential_inquiry_id}/credential_inquiry_responses/{id}`

This API endpoint can be used to delete an existing credential inquiry response. When the API call is successful, a success message will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| credential_inquiry_id | path | integer | true | The ID of the credential inquiry. You can find the credential inquiry ID by [fetching your credential inquiries](https://api.hackerone.com/customer-resources#credentials-get-credential-inquiries). |
| id | path | integer | true | The ID of the credential inquiry response. |

### Create a Credential Inquiry

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/credential_inquiries" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "structured_scope_id": 0,
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "structured_scope_id": 0,
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "structured_scope_id": 0,
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/credential_inquiries");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"structured_scope_id\": 0,\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/credential_inquiries", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential_inquiry created

```
{
  "data": {
    "id": "<id>",
    "type": "credential_inquiry",
    "attributes": {
      "description": "this is a credential inquiry"
    }
  }
}

```

Last revised: 2025-05-23

`POST /programs/{id}/credential_inquiries`

This API endpoint can be used to create new credential inquiry. When the API call is successful, a [credential_inquiry object](https://api.hackerone.com/customer-reference#credential_inquiry) will be returned. The IDs of a program's structured scopes can be retrieved from programs/{id}/structured_scopes endpoint.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| structured_scope_id | body | integer | true | The ID of the structured scope to which the credential will belong |
| data | body | object | true | The information to be requested from the hacker |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» description | body | string | true | A description of the information required from the hackers to create credentials |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | credential_inquiry |

### Get Credential Inquiries

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/credential_inquiries" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/credential_inquiries");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/credential_inquiries',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/credential_inquiries", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

data found with valid params

```
{
  "data": [
    {
      "id": "<id>",
      "type": "credential_inquiry",
      "attributes": {
        "description": "this is a credential inquiry"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/credential_inquiries`

Credential inquiries can be fetched by sending a GET request to the credential inquiries endpoint. When the request is successful, the API will respond with paginated [credential inquiry objects](https://api.hackerone.com/customer-customer-reference#credential_inquiry).

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Update Credential Inquiry

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "credential_inquiry",
    "attributes": {
      "description": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"credential_inquiry\",\n    \"attributes\": {\n      \"description\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

credential inquiry updated

```
{
  "data": {
    "id": "<id>",
    "type": "credential_inquiry",
    "attributes": {
      "description": "this is a credential inquiry"
    }
  }
}

```

Last revised: 2025-05-23

`PUT /programs/{program_id}/credential_inquiries/{id}`

This endpoint can be used to update a credential inquiry of a program. When the API request is successful, a [credential inquiry object](https://api.hackerone.com/customer-customer-reference#credential_inquiry) will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| id | path | integer | true | The ID of the credential inquiry. |
| data | body | object | true | The information to be requested from the hacker |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» description | body | string | true | A description of the information required from the hackers to create credentials |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | credential_inquiry |

### Delete Credential Inquiry

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/programs/{program_id}/credential_inquiries/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Credential Inquiry successfully removed

```
{
  "data": {
    "success": true,
    "message": "Credential Inquiry successfully removed"
  }
}

```

Last revised: 2025-05-23

`DELETE /programs/{program_id}/credential_inquiries/{id}`

This API endpoint can be used to delete an existing credential inquiry. When the API call is successful, a success message will be returned.

Required permissions: Team Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| id | path | integer | true | The ID of the credential inquiry. |

## Email

### Send email

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/email" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "email-message",
    "attributes": {
      "email": "string",
      "subject": "string",
      "markdown_content": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "email-message",
    "attributes": {
      "email": "string",
      "subject": "string",
      "markdown_content": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/email',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "email-message",
    "attributes": {
      "email": "string",
      "subject": "string",
      "markdown_content": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/email',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/email");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"email-message\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"subject\": \"string\",\n      \"markdown_content\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"email-message\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"subject\": \"string\",\n      \"markdown_content\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/email',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"email-message\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"subject\": \"string\",\n      \"markdown_content\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/email", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Email successfully sent

```
{
  "data": {
    "success": true,
    "message": "Email successfully sent"
  }
}

```

Last revised: 2025-09-01

`POST /email`

Send an email containing the defined markdown rendered as HTML.

Required permissions: The recipient must either share an organization with the API token or have an email address with a domain verified by the sender's organization, otherwise the email will not be sent. Insufficient permissions will result in a 400 Bad Request response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | Attributes that define an email message |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» email | body | string | true | The email address of the recipient. |
| »» subject | body | string | true | The subject of the email. |
| »» markdown_content | body | string | true | The body of the email. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | email-message |

## Hai

### Create Completion (Preview)

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/hai/chat/completions" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "completion-request",
    "attributes": {
      "hai_play_id": 0,
      "messages": [
        {
          "role": "user",
          "content": "string"
        }
      ],
      "program_handles": [
        "string"
      ],
      "report_ids": [
        0
      ],
      "cve_ids": [
        "string"
      ],
      "cwe_ids": [
        "string"
      ]
    }
  },
  "required": null
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "completion-request",
    "attributes": {
      "hai_play_id": 0,
      "messages": [
        {
          "role": "user",
          "content": "string"
        }
      ],
      "program_handles": [
        "string"
      ],
      "report_ids": [
        0
      ],
      "cve_ids": [
        "string"
      ],
      "cwe_ids": [
        "string"
      ]
    }
  },
  "required": null
}

r = requests.post(
  'https://api.hackerone.com/v1/hai/chat/completions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "completion-request",
    "attributes": {
      "hai_play_id": 0,
      "messages": [
        {
          "role": "user",
          "content": "string"
        }
      ],
      "program_handles": [
        "string"
      ],
      "report_ids": [
        0
      ],
      "cve_ids": [
        "string"
      ],
      "cwe_ids": [
        "string"
      ]
    }
  },
  "required": null
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/hai/chat/completions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/hai/chat/completions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"completion-request\",\n    \"attributes\": {\n      \"hai_play_id\": 0,\n      \"messages\": [\n        {\n          \"role\": \"user\",\n          \"content\": \"string\"\n        }\n      ],\n      \"program_handles\": [\n        \"string\"\n      ],\n      \"report_ids\": [\n        0\n      ],\n      \"cve_ids\": [\n        \"string\"\n      ],\n      \"cwe_ids\": [\n        \"string\"\n      ]\n    }\n  },\n  \"required\": null\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"completion-request\",\n    \"attributes\": {\n      \"hai_play_id\": 0,\n      \"messages\": [\n        {\n          \"role\": \"user\",\n          \"content\": \"string\"\n        }\n      ],\n      \"program_handles\": [\n        \"string\"\n      ],\n      \"report_ids\": [\n        0\n      ],\n      \"cve_ids\": [\n        \"string\"\n      ],\n      \"cwe_ids\": [\n        \"string\"\n      ]\n    }\n  },\n  \"required\": null\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/hai/chat/completions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"completion-request\",\n    \"attributes\": {\n      \"hai_play_id\": 0,\n      \"messages\": [\n        {\n          \"role\": \"user\",\n          \"content\": \"string\"\n        }\n      ],\n      \"program_handles\": [\n        \"string\"\n      ],\n      \"report_ids\": [\n        0\n      ],\n      \"cve_ids\": [\n        \"string\"\n      ],\n      \"cwe_ids\": [\n        \"string\"\n      ]\n    }\n  },\n  \"required\": null\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/hai/chat/completions", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

completion created

```
{
  "data": [
    {
      "id": "1",
      "type": "hai_chat_completion",
      "attributes": {
        "state": "created",
        "response": "This is a response",
        "created_at": "2019-01-01T00:00:00Z"
      }
    },
    {
      "id": "1",
      "type": "hai_chat_completion",
      "attributes": {
        "state": "generating",
        "response": null,
        "created_at": "2020-01-01T00:00:00Z"
      }
    }
  ]
}

```

Last revised: 2025-05-23

`POST /hai/chat/completions`

A POST request to create a [completion object](https://api.hackerone.com/customer-reference#hai-completion).

The feature is available for users whose organizations have [enabled Hai](https://docs.hackerone.com/en/articles/8887510-hai-ai-copilot#h_49672418da).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | The main data object containing the completion request details. |
| » type | body | string | false | The type of the request, which should be "completion-request". |
| » attributes | body | object | false | The attributes of the completion request. |
| »» hai_play_id | body | integer | false | The ID of the Hai Play to use for the completion. |
| »» messages | body | [object] | true | An array of message objects that form the conversation context. |
| »»» role | body | string | true | The role of the message sender, e.g., user or assistant. |
| »»» content | body | string | true | The content of the message. |
| »» program_handles | body | [string] | false | List of program handles associated with the completion request. |
| »» report_ids | body | [integer] | false | List of report IDs associated with the completion request. |
| »» cve_ids | body | [string] | false | List of CVE IDs associated with the completion request. |
| »» cwe_ids | body | [string] | false | List of CWE IDs associated with the completion request. |
| required | body | any | false | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | completion-request |
| »»» role | user |
| »»» role | assistant |

### Get Completions (Preview)

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/hai/chat/completions/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/hai/chat/completions/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/hai/chat/completions/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/hai/chat/completions/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/hai/chat/completions/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/hai/chat/completions/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

completion found

```
{
  "data": [
    {
      "id": "1",
      "type": "hai_chat_completion",
      "attributes": {
        "state": "created",
        "response": "This is a response",
        "created_at": "2019-01-01T00:00:00Z"
      }
    },
    {
      "id": "1",
      "type": "hai_chat_completion",
      "attributes": {
        "state": "generating",
        "response": null,
        "created_at": "2020-01-01T00:00:00Z"
      }
    }
  ]
}

```

Last revised: 2025-05-23

`GET /hai/chat/completions/{id}`

A GET request to retrieve and view a [completion object](https://api.hackerone.com/customer-reference#hai-completion) by its ID.

The feature is available for users whose organizations have [enabled Hai](https://docs.hackerone.com/en/articles/8887510-hai-ai-copilot#h_49672418da).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the completion. |

## Organizations

### Get Your Organizations

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/me/organizations" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/me/organizations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/me/organizations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/me/organizations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/me/organizations',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/me/organizations", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organizations found

```
{
  "data": [
    {
      "id": "1",
      "type": "organization",
      "attributes": {
        "handle": "security",
        "created_at": "2022-09-07T08:00:00.000Z",
        "updated_at": "2022-09-07T08:00:00.000Z"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /me/organizations`

This API endpoint allows you to query the [organization](https://api.hackerone.com/customer-reference#organization) objects that you are a member of.

The groups and members relationships are not included in the response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Audit Log

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{id}/audit_log" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{id}/audit_log',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{id}/audit_log',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{id}/audit_log");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{id}/audit_log',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{id}/audit_log", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Audit logs

```
{
  "data": [
    {
      "id": "2037",
      "type": "audit-log-item",
      "attributes": {
        "log": "\"@jobert\" updated member with role \"member\" from organization \"Yahoo!\".",
        "event": "organizations.members.update",
        "source": "User#1",
        "subject": "Member#123",
        "user_agent": "Chrome/133.0.0.0",
        "country": "US",
        "parameters": {
          "previous_role": "viewer",
          "new_role": "member"
        },
        "created_at": "2025-02-25T12:28:07.041Z"
      },
      "relationships": {
        "source_user": {
          "id": "7",
          "type": "user",
          "attributes": {
            "username": "jobert",
            "name": "Jobert Abma",
            "disabled": false,
            "created_at": "2025-01-21T20:08:39.887Z",
            "profile_picture": {
              "62x62": "http://localhost:3000/rails/active_storage/representations/redirect/avatar_jobert_62.png",
              "82x82": "http://localhost:3000/rails/active_storage/representations/redirect/avatar_jobert_82.png",
              "110x110": "http://localhost:3000/rails/active_storage/representations/redirect/avatar_jobert_110.png",
              "260x260": "http://localhost:3000/rails/active_storage/representations/redirect/avatar_jobert_260.png"
            }
          }
        }
      }
    }
  ]
}

```

Last revised: 2025-05-23

`GET /organizations/{id}/audit_log`

Returns a paginated list of the audit log items of the provided organization.

This API endpoint allows a user to view all audit log items that have been created for a particular organization.

Required permissions: Organization Management. You can view audit log items and manage the permissions of your API users through your organization's settings. Insufficient permissions will result in the data being returned as an empty array.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get All Eligibility Settings

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization eligibility settings found

```
{
  "data": [
    {
      "id": "1",
      "type": "eligibility-setting",
      "attributes": {
        "allowed_domains": [
          "hackerone.com"
        ],
        "allowed_domains_enabled": true,
        "name": "Organization Eligibility Settings",
        "organization_id": "1",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z"
      }
    }
  ]
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/eligibility_settings`

This API endpoint can be used to list all eligibility settings of an organization. When the request is successful, the API will respond with paginated [eligibility-setting](https://api.hackerone.com/customer-reference#eligibility-setting).

Required permissions: Group Manager or User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Eligibility Setting

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/eligibility_settings/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

eligibility setting successfully fetched from organization

```
{
  "data": {
    "id": "1",
    "type": "eligibility-setting",
    "attributes": {
      "allowed_domains": [
        "hackerone.com"
      ],
      "allowed_domains_enabled": true,
      "name": "Organization Eligibility Settings",
      "organization_id": "1",
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z"
    }
  }
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/eligibility_settings/{id}`

This API endpoint can be used to get an eligibility_setting of an organization. When the request is successful, the API will respond with [eligibility-setting object](https://api.hackerone.com/customer-reference#eligibility-setting).

Required permissions: Group Manager or User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the eligibility setting. |

### Get All Inboxes

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/inboxes" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/inboxes',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/inboxes',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/inboxes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/inboxes',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/inboxes", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization inboxes found

```
{
  "data": [
    {
      "id": "<id>",
      "type": "inbox",
      "attributes": {
        "name": "Inbox 1"
      }
    },
    {
      "id": "<id>",
      "type": "inbox",
      "attributes": {
        "name": "Custom Inbox 2"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/inboxes`

This API endpoint can be used to list all inboxes of an organization. When the request is successful, the API will respond with paginated [inbox objects](https://api.hackerone.com/customer-reference#inbox).

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Pending Invitations

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/pending_invitations", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

invitation found

```
{
  "data": [
    {
      "type": "invitation-organization-member",
      "id": "1",
      "attributes": {
        "email": "example@hackerone.com",
        "username": null,
        "invited_by_id": "2",
        "recipient_id": null,
        "invitation_data": {
          "notify": true,
          "organization_admin": true,
          "organization_member_group_ids": []
        },
        "expires_at": "2016-02-02T04:05:06.000Z",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z"
      }
    }
  ]
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/pending_invitations`

This API endpoint can be used to list all open invitations of an organization. When the request is successful, the API will respond with paginated [invitation-organization-member objects](https://api.hackerone.com/customer-reference#invitation-organization-member).

Required permissions: User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create An Invitation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/invitations" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "invitation-organization-member",
    "attributes": {
      "email": "string",
      "organization_member_group_ids": [],
      "organization_admin": true,
      "notify": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "invitation-organization-member",
    "attributes": {
      "email": "string",
      "organization_member_group_ids": [],
      "organization_admin": true,
      "notify": true
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/invitations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "invitation-organization-member",
    "attributes": {
      "email": "string",
      "organization_member_group_ids": [],
      "organization_admin": true,
      "notify": true
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/invitations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/invitations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"invitation-organization-member\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"organization_member_group_ids\": [],\n      \"organization_admin\": true,\n      \"notify\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"invitation-organization-member\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"organization_member_group_ids\": [],\n      \"organization_admin\": true,\n      \"notify\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/invitations',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"invitation-organization-member\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"organization_member_group_ids\": [],\n      \"organization_admin\": true,\n      \"notify\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/invitations", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

invitation created

```
{
  "data": {
    "type": "invitation-organization-member",
    "id": "1",
    "attributes": {
      "email": "example@hackerone.com",
      "username": null,
      "invited_by_id": "2",
      "recipient_id": null,
      "invitation_data": {
        "notify": true,
        "organization_admin": true,
        "organization_member_group_ids": []
      },
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "expires_at": "2016-02-02T04:05:06.000Z"
    }
  }
}

```

Last revised: 2025-05-23

`POST /organizations/{organization_id}/invitations`

This API endpoint can be used to invite a recipient to an organization using their email address. This endpoint can trigger notifications. When the request is successful, the API will respond with an [invitation-organization-member](https://api.hackerone.com/customer-reference#invitation-organization-member) object.

Required permissions: User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| data | body | object | true | The information to create the organization member invitation. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» email | body | string | true | The invitee email. It must respect the eligibility settings of the groups and the organization. |
| »» organization_member_group_ids | body | array | false | The organization groups IDs where the user should be added. |
| »» organization_admin | body | boolean | false | Sets the invitee as an organization admin. |
| »» notify | body | boolean | false | Activates organization notifications for the invitee. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | invitation-organization-member |

### Get Group

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization member group found

```
{
  "data": {
    "id": "<id>",
    "type": "organization-member-group",
    "attributes": {
      "name": "Standard2",
      "organization_id": "<id>",
      "eligibility_setting_id": "<id>",
      "permissions": [
        "read_only_member"
      ],
      "created_at": "<date>",
      "updated_at": "<date>",
      "migrated_at": null
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": "<id>",
            "type": "organization-member",
            "attributes": {
              "organization_id": "<id>",
              "user_id": "<id>",
              "email": "user2@hackerone.com",
              "organization_admin": true,
              "created_at": "<date>",
              "updated_at": "<date>",
              "last_sign_in_at": "<date>",
              "system": false,
              "username": "user2"
            }
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": "<id>",
            "type": "program",
            "attributes": {
              "handle": "program",
              "created_at": "<date>",
              "updated_at": "<date>"
            }
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": "<id>",
            "type": "inbox",
            "attributes": {
              "name": "default inbox for inbox",
              "type": "default"
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/groups/{id}`

This API endpoint can be used to get a group of an organization. When the request is successful, the API will respond with [organization-member-group object](https://api.hackerone.com/customer-reference#organization-member-group).

Required permissions: Group Manager or User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the group. |

### Update Group

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "eligibility_setting_id": 0,
      "permissions": [
        "string"
      ]
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "eligibility_setting_id": 0,
      "permissions": [
        "string"
      ]
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "eligibility_setting_id": 0,
      "permissions": [
        "string"
      ]
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"eligibility_setting_id\": 0,\n      \"permissions\": [\n        \"string\"\n      ]\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"eligibility_setting_id\": 0,\n      \"permissions\": [\n        \"string\"\n      ]\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"eligibility_setting_id\": 0,\n      \"permissions\": [\n        \"string\"\n      ]\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/organizations/{organization_id}/groups/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization member group updated

```
{
  "data": {
    "id": "<id>",
    "type": "organization-member-group",
    "attributes": {
      "name": "Standard3",
      "organization_id": "<id>",
      "eligibility_setting_id": "<id>",
      "permissions": [
        "report_analyst",
        "read_only_member"
      ],
      "created_at": "<date>",
      "updated_at": "<date>",
      "migrated_at": null
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": "<id>",
            "type": "organization-member",
            "attributes": {
              "organization_id": "<id>",
              "user_id": "<id>",
              "email": "user@hackerone.com",
              "organization_admin": false,
              "created_at": "<date>",
              "updated_at": "<date>",
              "last_sign_in_at": "<date>",
              "system": false,
              "username": "user"
            }
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": "<id>",
            "type": "program",
            "attributes": {
              "handle": "user-management-api",
              "created_at": "<date>",
              "updated_at": "<date>"
            }
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": "<id>",
            "type": "inbox",
            "attributes": {
              "name": "User management api inbox",
              "type": "default"
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-05-23

`PUT /organizations/{organization_id}/groups/{id}`

This endpoint can be used to update an organization member group. When the API request is successful, an [organization member group object](https://api.hackerone.com/customer-reference#organization-member-group) will be returned.

It is possible to update members and programs users have access to via`organization_members` and`programs` relationships.

Required permissions: Group Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the organization member group. |
| data | body | object | true | The information to update an organization member. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | false | The name of the organization member group. |
| »» eligibility_setting_id | body | integer | false | The ID of the eligibility setting. |
| »» permissions | body | [string] | false | The permissions added to the new organization group. Possible values are: asset_inventory_manager, asset_inventory_viewer, group_manager, program_admin, read_only_member, report_analyst, report_reward_manager and user_manager. |
| » relationships | body | object | false | none |
| »» organization_members | body | object | false | A list of members for the organization member group. |
| »»» data | body | [any] | true | none |
| »» programs | body | object | false | A list of programs for the organization member group. |
| »»» data | body | [any] | true | none |
| »» inboxes | body | object | false | A list of inboxes for the organization member group. |
| »»» data | body | [any] | true | none |

Detailed descriptions

»» programs: A list of programs for the organization member group.

Ensure that when adding a program, the related inbox is also added to the group.

You can retrieve all inboxes of an organization through the [get all inboxes](https://api.hackerone.com/customer-resources#organizations-get-all-inboxes) endpoint.

»» inboxes: A list of inboxes for the organization member group.

Ensure that when adding a non- [custom inbox](https://docs.hackerone.com/en/articles/8519260-custom-inboxes), the related program is also added to the group.

You can retrieve all programs of an organization through the [get all programs](https://api.hackerone.com/customer-resources#organizations-get-all-programs) endpoint.

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | organization-member-group |

### Get All Groups

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/groups" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/groups',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/groups',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/groups");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/groups',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/groups", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization member groups found

```
{
  "data": [
    {
      "id": "<id>",
      "type": "organization-member-group",
      "attributes": {
        "name": "User managers",
        "organization_id": "<id>",
        "eligibility_setting_id": null,
        "permissions": [
          "group_manager"
        ],
        "created_at": "<date>",
        "updated_at": "<date>",
        "migrated_at": null
      }
    },
    {
      "id": "<id>",
      "type": "organization-member-group",
      "attributes": {
        "name": "Standard1",
        "organization_id": "<id>",
        "eligibility_setting_id": "<id>",
        "permissions": [
          "read_only_member"
        ],
        "created_at": "<date>",
        "updated_at": "<date>",
        "migrated_at": null
      }
    },
    {
      "id": "<id>",
      "type": "organization-member-group",
      "attributes": {
        "name": "Standard2",
        "organization_id": "<id>",
        "eligibility_setting_id": "<id>",
        "permissions": [
          "read_only_member"
        ],
        "created_at": "<date>",
        "updated_at": "<date>",
        "migrated_at": null
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/groups`

This API endpoint can be used to list all groups of an organization. When the request is successful, the API will respond with paginated [organization-member-group objects](https://api.hackerone.com/customer-reference#organization-member-group).

Required permissions: Group Manager or User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create Group

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/groups" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "permissions": [],
      "eligibility_setting_id": 0
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "permissions": [],
      "eligibility_setting_id": 0
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/groups',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "organization-member-group",
    "attributes": {
      "name": "string",
      "permissions": [],
      "eligibility_setting_id": 0
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": 0,
            "type": "organization-member"
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": 0,
            "type": "inbox"
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/groups',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/groups");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"permissions\": [],\n      \"eligibility_setting_id\": 0\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"permissions\": [],\n      \"eligibility_setting_id\": 0\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/groups',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"organization-member-group\",\n    \"attributes\": {\n      \"name\": \"string\",\n      \"permissions\": [],\n      \"eligibility_setting_id\": 0\n    },\n    \"relationships\": {\n      \"organization_members\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member\"\n          }\n        ]\n      },\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      },\n      \"inboxes\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"inbox\"\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/groups", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization group created

```
{
  "data": {
    "id": "<id>",
    "type": "organization-member-group",
    "attributes": {
      "name": "organization_member_group4",
      "organization_id": "<id>",
      "eligibility_setting_id": null,
      "permissions": [
        "read_only_member"
      ],
      "created_at": "<date>",
      "updated_at": "<date>",
      "migrated_at": null
    },
    "relationships": {
      "organization_members": {
        "data": [
          {
            "id": "<id>",
            "type": "organization-member",
            "attributes": {
              "organization_id": "<id>",
              "user_id": "<id>",
              "email": "user4@hackerone.com",
              "organization_admin": false,
              "created_at": "<date>",
              "updated_at": "<date>",
              "last_sign_in_at": "<date>",
              "system": false,
              "username": "user4"
            }
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": "<id>",
            "type": "program",
            "attributes": {
              "handle": "user-management-api",
              "created_at": "<date>",
              "updated_at": "<date>"
            }
          }
        ]
      },
      "inboxes": {
        "data": [
          {
            "id": "<id>",
            "type": "inbox",
            "attributes": {
              "name": "User management api inbox",
              "type": "default"
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /organizations/{organization_id}/groups`

This API endpoint can be used to create a new organization group. When the request is successful the API will respond with an [organization group object](https://api.hackerone.com/customer-reference#organization-member-group).

It is possible to add users to the new organization group by including a list of organization members as relationships. A list of organization members can be obtained at organizations/{organization_id}/members

It is possible to add programs to the new organization group by including a list of programs as relationships.

Required permissions: Group Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| data | body | object | true | The information to create the organization group. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | true | The name of the new organization group. |
| »» permissions | body | array | true | The permissions added to the new organization group. Possible values are: asset_inventory_manager, asset_inventory_viewer, group_manager, program_admin, read_only_member, report_analyst, report_reward_manager and user_manager. |
| »» eligibility_setting_id | body | integer | false | The id of the eligibility settings. |
| » relationships | body | object | false | none |
| »» organization_members | body | object | false | A list of members for the organization member group. |
| »»» data | body | [any] | true | none |
| »» programs | body | object | false | A list of programs for the organization member group. |
| »»» data | body | [any] | true | none |
| »» inboxes | body | object | false | A list of inboxes for the organization member group. |
| »»» data | body | [any] | true | none |

Detailed descriptions

»» programs: A list of programs for the organization member group.

Ensure that when adding a program, the related inbox is also added to the group.

You can retrieve all inboxes of an organization through the [get all inboxes](https://api.hackerone.com/customer-resources#organizations-get-all-inboxes) endpoint.

»» inboxes: A list of inboxes for the organization member group.

Ensure that when adding a non- [custom inbox](https://docs.hackerone.com/en/articles/8519260-custom-inboxes), the related program is also added to the group.

You can retrieve all programs of an organization through the [get all programs](https://api.hackerone.com/customer-resources#organizations-get-all-programs) endpoint.

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | organization-member-group |

### Get All Members

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/members" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/members',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/members',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/members");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/members',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/members", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization members found

```
{
  "data": [
    {
      "id": "1",
      "type": "organization-member",
      "attributes": {
        "organization_id": "3",
        "user_id": "5",
        "email": "example@hackerone.com",
        "organization_admin": true,
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z",
        "last_sign_in_at": "2023-11-24T21:24:31.102Z",
        "system": false,
        "username": "api-example"
      },
      "relationships": {
        "organization_member_groups": {
          "data": [
            {
              "id": "2",
              "type": "organization-member-group",
              "attributes": {
                "name": "Standard1",
                "organization_id": "3",
                "eligibility_setting_id": "4",
                "permissions": [
                  "read_only_member"
                ],
                "created_at": "2016-02-02T04:05:06.000Z",
                "updated_at": "2016-02-02T04:05:06.000Z",
                "migrated_at": null
              }
            }
          ]
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-11-25

`GET /organizations/{organization_id}/members`

This API endpoint can be used to list all members of an organization. When the request is successful, the API will respond with paginated [organization member objects](https://api.hackerone.com/customer-reference#organization-member).

Required permissions: User Manager or Groups Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 401 Unauthorized response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Member

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

member successfully fetched from organization

```
{
  "data": {
    "id": "1",
    "type": "organization-member",
    "attributes": {
      "organization_id": "3",
      "user_id": "5",
      "email": "example@hackerone.com",
      "organization_admin": true,
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "last_sign_in_at": "2023-11-24T21:24:31.102Z",
      "system": false,
      "username": "api-example"
    },
    "relationships": {
      "organization_member_groups": {
        "data": [
          {
            "id": "2",
            "type": "organization-member-group",
            "attributes": {
              "name": "Standard1",
              "organization_id": "3",
              "eligibility_setting_id": "4",
              "permissions": [
                "read_only_member"
              ],
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "migrated_at": null
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-11-25

`GET /organizations/{organization_id}/members/{id}`

This API endpoint can be used to get a member of an organization. When the request is successful, the API will respond with [organization-member object](https://api.hackerone.com/customer-reference#organization-member).

Required permissions: User Manager or Groups Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 401 Unauthorized response.

You can get the ID of your organization from me/organizations endpoint.

You can get the IDs of your organization members from get all members endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the member. |

### Remove Member

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

member successfully removed from organization

```
{
  "data": {
    "success": true,
    "message": "Member successfully removed from organization"
  }
}

```

Last revised: 2025-11-25

`DELETE /organizations/{organization_id}/members/{id}`

This API endpoint can be used to delete a member of an organization. When the request is successful, the API will respond with a successfully message.

Required permissions: User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 401 Unauthorized response.

Trying to remove an organization admin with an api token that is not an organization admin will return error 403 Forbidden.

You can get the ID of your organization from me/organizations endpoint.

You can get the IDs of your organization members from get all members endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the member. |

### Update Member

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "organization-member",
    "attributes": {
      "organization_admin": true
    },
    "relationships": {
      "organization_member_groups": {
        "data": [
          {
            "id": 0,
            "type": "organization-member-group"
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "organization-member",
    "attributes": {
      "organization_admin": true
    },
    "relationships": {
      "organization_member_groups": {
        "data": [
          {
            "id": 0,
            "type": "organization-member-group"
          }
        ]
      }
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "organization-member",
    "attributes": {
      "organization_admin": true
    },
    "relationships": {
      "organization_member_groups": {
        "data": [
          {
            "id": 0,
            "type": "organization-member-group"
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"organization-member\",\n    \"attributes\": {\n      \"organization_admin\": true\n    },\n    \"relationships\": {\n      \"organization_member_groups\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member-group\"\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"organization-member\",\n    \"attributes\": {\n      \"organization_admin\": true\n    },\n    \"relationships\": {\n      \"organization_member_groups\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member-group\"\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"organization-member\",\n    \"attributes\": {\n      \"organization_admin\": true\n    },\n    \"relationships\": {\n      \"organization_member_groups\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"organization-member-group\"\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/organizations/{organization_id}/members/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization member updated

```
{
  "data": {
    "id": "1",
    "type": "organization-member",
    "attributes": {
      "organization_id": "3",
      "user_id": "5",
      "email": "example@hackerone.com",
      "organization_admin": true,
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "last_sign_in_at": "2023-11-24T21:24:31.102Z",
      "system": false,
      "username": "api-example"
    },
    "relationships": {
      "organization_member_groups": {
        "data": [
          {
            "id": "2",
            "type": "organization-member-group",
            "attributes": {
              "name": "Standard1",
              "organization_id": "3",
              "eligibility_setting_id": "4",
              "permissions": [
                "read_only_member"
              ],
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "migrated_at": null
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2025-11-25

`PUT /organizations/{organization_id}/members/{id}`

This endpoint can be used to update an organization member. When the API request is successful, an [organization member object](https://api.hackerone.com/customer-reference#organization-member) will be returned.

It is possible to update groups users have access to via`organization_member_groups` relationships.

Required permissions: User Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 401 Unauthorized response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| id | path | integer | true | The ID of the organization member. |
| data | body | object | true | The information to update an organization member. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» organization_admin | body | boolean | false | If the member is an organization admin. |
| » relationships | body | object | false | none |
| »» organization_member_groups | body | object | false | A list of groups for the organization member. |
| »»» data | body | [any] | true | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | organization-member |

### Get All Programs

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/programs" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/programs',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/programs',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/programs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/programs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/programs", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

organization programs found

```
{
  "data": [
    {
      "id": "<id>",
      "type": "program",
      "attributes": {
        "handle": "user-management-api",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z"
      }
    },
    {
      "id": "<id>",
      "type": "program",
      "attributes": {
        "handle": "user-management-api-2",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/programs`

This API endpoint can be used to list all programs of an organization. When the request is successful, the API will respond with paginated [program objects](https://api.hackerone.com/customer-reference#program_small).

Required permissions: Group Manager. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

## Programs

### Get Your Programs

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/me/programs" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/me/programs',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/me/programs',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/me/programs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/me/programs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/me/programs", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

programs found

```
{
  "data": [
    {
      "id": "1",
      "type": "program",
      "attributes": {
        "handle": "security",
        "created_at": "2017-01-01T08:00:00.000Z",
        "updated_at": "2017-02-17T04:34:15.910Z"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /me/programs`

This API endpoint allows you to query the [program](https://api.hackerone.com/customer-reference#program) objects that you are a member of.

The groups and members relationships are not included in the response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Allowed Reporter Activities

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/activities", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

activities found

```
{
  "data": [
    {
      "type": "activity-program-hacker-joined",
      "id": "1337",
      "attributes": {
        "message": "",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z",
        "internal": false
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/allowed_reporters/{allowed_reporter_id}/activities`

This resource allows you to retrieve a list of activities of a researcher that belong to your private program.

These activities are "activity-program-hacker-joined", "activity-program-hacker-left" and "activity-invitation-received"

Multiple activities objects can be queried by sending a GET request to the reporters endpoint. When the request is successful, the API will respond with paginated [activities objects](https://api.hackerone.com/customer-reference#activity). Note that, you won't see other relationships and attachments of an activity.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| allowed_reporter_id | path | integer | true | The ID of the allowed reporter. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Allowed Reporter username history

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

allowed reporter found

```
{
  "data": {
    "type": "allowed_reporter_username_history",
    "attributes": {
      "old_usernames": [
        "zero-trust",
        "zero_trust-the-sequel"
      ],
      "user_id": "42"
    }
  }
}

```

Last revised: 2025-05-23

`GET /programs/{id}/allowed_reporters/{allowed_reporter_id}/username_history`

This resource allows you to retrieve a list of old usernames of a researcher that belong to your private program.

This can be useful for debugging purposes, but HackerOne advises to rely on IDs for cross-referencing data (instead of usernames) The current username is not included in the list.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| allowed_reporter_id | path | integer | true | The ID of the allowed reporter. |

### Get Allowed Reporters

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/allowed_reporters" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/allowed_reporters',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/allowed_reporters',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/allowed_reporters");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/allowed_reporters',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/allowed_reporters", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

allowed reporters found

```
{
  "data": [
    {
      "id": "1337",
      "type": "allowed_reporter",
      "attributes": {
        "username": "awesome-hacker",
        "email_alias": "awesome-hacker@wearehackerone.com",
        "rules_of_engagement_signed": true,
        "identity_verified": true,
        "background_checked": true,
        "cleared": true,
        "citizenship_verified": false,
        "residency_verified": true,
        "created_at": "2016-02-02T04:05:06.000Z"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/allowed_reporters`

This resource allows you to retrieve a list of all researchers that belong to your private program.

Multiple allowed reporter objects can be queried by sending a GET request to the reporters endpoint. When the request is successful, the API will respond with paginated [allowed reporter objects](https://api.hackerone.com/customer-reference#allowed_reporter).

Required permissions: Program Management. You can view audit log items and manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Allowed Reporters History

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/allowed_reporters_history", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

allowed reporters history found

```
{
  "data": [
    {
      "id": "5",
      "type": "allowed-reporter-history-entry",
      "attributes": {
        "created_at": "2025-02-13T20:12:45.624Z",
        "invited_at": "2025-01-10T20:12:45.624Z",
        "accepted_at": "2025-02-13T20:12:45.624Z",
        "left_at": "2025-03-13T20:12:45.624Z",
        "removed_at": null
      },
      "relationships": {
        "user": {
          "id": "5",
          "type": "user",
          "attributes": {
            "username": "demo-hacker",
            "name": "Demo Researcher",
            "disabled": false,
            "created_at": "2025-02-10T20:10:27.242Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default-14ffa99f59cd01423c64904352cc130ffcb6a802eadfd11777a54485749e60f2.png",
              "82x82": "/assets/avatars/default-14ffa99f59cd01423c64904352cc130ffcb6a802eadfd11777a54485749e60f2.png",
              "110x110": "/assets/avatars/default-14ffa99f59cd01423c64904352cc130ffcb6a802eadfd11777a54485749e60f2.png",
              "260x260": "/assets/avatars/default-14ffa99f59cd01423c64904352cc130ffcb6a802eadfd11777a54485749e60f2.png"
            },
            "signal": null,
            "impact": null,
            "reputation": null,
            "bio": null,
            "website": null,
            "location": null,
            "hackerone_triager": false
          }
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/allowed_reporters_history`

This resource allows you to retrieve a list of [allowed reporter history entries](https://api.hackerone.com/customer-reference#allowed-reporter-history-entry), containing all researchers who joined/left your private program.

Required permissions: Program Management. You can view audit log items and manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |
| sort | query | any | false | The attributes to sort the allowed reporters history entries on. |
| order | query | any | false | The direction to sort the allowed reporters history entries on, by default asc. |

Detailed descriptions

sort: The attributes to sort the allowed reporters history entries on.

Sorting is applied based according to the value defined in the order parameter.

The following values can be used for sorting: id, created_at, invited_at, accepted_at, left_at, removed_at.

order: The direction to sort the allowed reporters history entries on, by default asc.

The following values can be used for sorting: asc (ascending), desc (descending).

Enumerated Values

| Parameter | Value |
| --- | --- |
| sort | id |
| sort | created_at |
| sort | invited_at |
| sort | accepted_at |
| sort | left_at |
| sort | removed_at |
| order | asc |
| order | desc |

### Get Audit Log

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/audit_log" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/audit_log',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/audit_log',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/audit_log");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/audit_log',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/audit_log", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Audit logs

```
{
  "data": {
    "id": "1",
    "type": "audit-log-item",
    "attributes": {
      "log": "\"@member\" invited \"someone@example.com\".",
      "event": "invitations.team_members.create",
      "source": "User#1",
      "subject": "Invitation#1",
      "user_agent": "Chrome/11.0",
      "country": "US",
      "parameters": "{\"identifier\":\"jobert\"}",
      "created_at": "2019-05-15T04:05:06.000Z"
    }
  }
}

```

Last revised: 2025-05-23

`GET /programs/{id}/audit_log`

Returns a paginated list of the audit log items of the provided program.

This API endpoint allows a user to view all [audit log items](https://api.hackerone.com/customer-reference#audit-log) that have been created for a particular program.

Required permissions: Program Management. You can view audit log items and manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Your Programs Balance

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/billing/balance" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/billing/balance',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/billing/balance',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/billing/balance");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/billing/balance',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/billing/balance", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

balance found

```
{
  "data": {
    "id": "1337",
    "type": "program-balance",
    "attributes": {
      "balance": "1500.00"
    }
  }
}

```

Last revised: 2025-05-23

`GET /programs/{id}/billing/balance`

This API endpoint allows a user to retrieve the current balance for a particular program.

Required permissions: Program Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Get Payment Transactions

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/billing/transactions" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/billing/transactions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/billing/transactions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/billing/transactions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/billing/transactions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/billing/transactions", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Payment transactions found

```
{
  "id": 10,
  "bounty_award": "1000.00",
  "bounty_fee": "200.00",
  "activity_date": "2019-09-25T04:22:42.686Z",
  "activity_description": "Bounty for report #9",
  "debit_or_credit_amount": "-1200.00",
  "balance": "-1200.00",
  "payment_transaction_type": "payment",
  "relationships": {
    "payer": {
      "data": {
        "id": 3,
        "type": "user"
      },
      "attributes": {
        "username": "payer-username"
      },
      "links": {
        "self": "http://hackerone.com/payer-username"
      }
    },
    "report": {
      "data": {
        "id": 9,
        "type": "report"
      },
      "links": {
        "self": "http://hackerone.com/reports/9"
      }
    },
    "user": {
      "data": {
        "id": 1,
        "type": "user"
      },
      "attributes": {
        "username": "hacker-username"
      },
      "links": {
        "self": "http://hackerone.com/hacker-username"
      }
    },
    "team": {
      "data": {
        "id": 2,
        "type": "team"
      },
      "attributes": {
        "handle": "hacker-team"
      },
      "links": {
        "self": "http://hackerone.com/hacker-team"
      }
    }
  },
  "links": {
    "self": "https://api.hackerone.com/v1/programs/{id}/billing/transactions?page%5Bnumber%5D=1",
    "next": "https://api.hackerone.com/v1/programs/{id}/billing/transactions?page%5Bnumber%5D=2",
    "last": "https://api.hackerone.com/v1/programs/{id}/billing/transactions?page%5Bnumber%5D=5"
  }
}

```

Last revised: 2025-05-23

`GET /programs/{id}/billing/transactions`

This API endpoint enables a user to retrieve program's list of payment transactions for the selected month. When the request is successful, the API will respond with paginated [payment transaction](https://api.hackerone.com/customer-reference#transaction) objects of the provided program.

If you want to get transactions for an entire year, you will need to request each month individually.

Required permissions: Program Management. You can manage the permissions of your API users through your program's settings. If the program has a parent program, the API user should belong to the parent program. Insufficient permissions will result in a 403 Forbidden or a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| month | query | integer | false | The month of the transaction period. The default is set to the current month. |
| year | query | integer | false | The year of the transaction period. The default is set to the current year. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Award Bounty

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/bounties" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "bounty",
    "attributes": {
      "recipient": "string",
      "recipient_id": "string",
      "amount": 0,
      "reference": "string",
      "title": "string",
      "currency": "USD",
      "severity_rating": "none"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "bounty",
    "attributes": {
      "recipient": "string",
      "recipient_id": "string",
      "amount": 0,
      "reference": "string",
      "title": "string",
      "currency": "USD",
      "severity_rating": "none"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/bounties',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "bounty",
    "attributes": {
      "recipient": "string",
      "recipient_id": "string",
      "amount": 0,
      "reference": "string",
      "title": "string",
      "currency": "USD",
      "severity_rating": "none"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/bounties',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/bounties");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient\": \"string\",\n      \"recipient_id\": \"string\",\n      \"amount\": 0,\n      \"reference\": \"string\",\n      \"title\": \"string\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"none\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient\": \"string\",\n      \"recipient_id\": \"string\",\n      \"amount\": 0,\n      \"reference\": \"string\",\n      \"title\": \"string\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"none\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/bounties',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient\": \"string\",\n      \"recipient_id\": \"string\",\n      \"amount\": 0,\n      \"reference\": \"string\",\n      \"title\": \"string\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"none\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/bounties", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

bounty awarded

```
{
  "data": {
    "id": "1",
    "type": "bounty",
    "attributes": {
      "amount": "100.00",
      "bonus_amount": "0.00",
      "awarded_amount": "100.00",
      "awarded_bonus_amount": "0.00",
      "awarded_currency": "USD",
      "created_at": "2017-02-14T23:07:24.252Z"
    },
    "relationships": {
      "report": {
        "data": {
          "id": "1337",
          "type": "report",
          "attributes": {
            "title": "XSS in login form",
            "state": "new",
            "created_at": "2016-02-02T04:05:06.000Z",
            "vulnerability_information": "...",
            "triaged_at": null,
            "closed_at": null,
            "last_reporter_activity_at": null,
            "first_program_activity_at": null,
            "last_program_activity_at": null,
            "bounty_awarded_at": null,
            "swag_awarded_at": null,
            "disclosed_at": null,
            "last_public_activity_at": null,
            "last_activity_at": null,
            "issue_tracker_reference_url": "https://example.com/reference",
            "cve_ids": [],
            "source": null,
            "reporter_agreed_on_going_public_at": null
          }
        }
      },
      "invitations": [
        {
          "id": "10",
          "recipient": "hacker@hackerone.com",
          "claim_url": "https://hackerone.com/invitations/3fe0a8badea0023c2fcca5c860d5899e"
        }
      ]
    }
  }
}

```

Last revised: 2025-05-23

`POST /programs/{id}/bounties`

Use this endpoint to award a bounty. When the API call is successful, a [bounty](https://api.hackerone.com/customer-reference#bounty) object will be returned.

Required permissions: Reward Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information required to create a bounty. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» recipient | body | string | false | The email address of the recipient. |
| »» recipient_id | body | string | false | The id of the recipient. |
| »» amount | body | number | true | The bounty amount to be awarded. |
| »» reference | body | string | true | An internal reference attached to the report that makes searching or filtering in the future easy. |
| »» title | body | string | true | The title of the security vulnerability that was reported to you. |
| »» currency | body | string | true | none |
| »» severity_rating | body | [severity-ratings](https://api.hackerone.com/customer-reference#severity-ratings) | false | The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score. |

Detailed descriptions

»» recipient: The email address of the recipient.

When the email address is provided, an email will be sent to the recipient to claim the bounty. When the email address is not provided, you can use the claim URL in the response to notify the recipient yourself. When the user does not have an account yet with HackerOne, they'll be onboarded before they can claim the reward. Users that already have an account, will benefit from collecting the payout easily through HackerOne and will get additional reputation points to showcase on their HackerOne profile.

»» recipient_id: The id of the recipient.

When the recipient_id is provided, an email will be sent to the recipient to claim the bounty. If both recipient and recipient_id provided then recipient attribute has a higher priority. If non of attributes provided then email won't be sent.

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | bounty |
| »» currency | USD |
| »» severity_rating | none |
| »» severity_rating | low |
| »» severity_rating | medium |
| »» severity_rating | high |
| »» severity_rating | critical |

### Get Bounty Table

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/bounty_table" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/bounty_table',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/bounty_table',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/bounty_table");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/bounty_table',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/bounty_table", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

bounty table found

```
{
  "data": {
    "id": "1",
    "type": "bounty-table",
    "attributes": {
      "description": "description",
      "low_label": "Low",
      "medium_label": "Medium",
      "high_label": "High",
      "critical_label": "Critical",
      "use_range": false,
      "updated_at": "2016-02-02T04:05:06.000Z"
    },
    "relationships": {
      "bounty_table_rows": {
        "data": [
          {
            "id": "1",
            "type": "bounty-table-row",
            "attributes": {
              "name": null,
              "description": null,
              "low": 1,
              "low_minimum": 0,
              "medium": 2,
              "medium_minimum": 1,
              "high": 3,
              "high_minimum": 2,
              "critical": 4,
              "critical_minimum": 3,
              "use_range": false,
              "updated_at": "2016-02-02T04:05:06.000Z"
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2026-04-10

`GET /programs/{id}/bounty_table`

The bounty table endpoint enables you to retrieve the active bounty table for a program, including all bounty table rows with their severity-based reward amounts.

When the request is successful, the API will respond with a bounty table object containing its rows. Each row defines the reward amounts (or ranges) per severity level. If the program does not have a bounty table, the API will respond with a 404 Not Found.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Get All Campaigns

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/campaigns" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/campaigns',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/campaigns',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/campaigns");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/campaigns',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/campaigns", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaigns found

```
{
  "data": [
    {
      "id": "<id>",
      "type": "campaign",
      "attributes": {
        "campaign_type": "multiplier",
        "researchers_information": "Focus on authentication bypass vulnerabilities",
        "critical": 2,
        "high": 1.5,
        "medium": 1.5,
        "low": 1,
        "bounty_pool_limit": null,
        "start_date": "2026-04-01T01:00:00.000Z",
        "end_date": "2026-04-10T23:00:00.000Z",
        "status": "scheduled",
        "target_audience": false,
        "extended_at": null,
        "total_reports": 0,
        "valid_reports": 0,
        "total_critical_reports": 0,
        "total_high_reports": 0,
        "bounty_spent": 0
      },
      "relationships": {
        "campaign_objective": {
          "data": {
            "id": "<id>",
            "type": "campaign-objective",
            "attributes": {
              "name": "Test new asset",
              "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
              "category": "newest_changes",
              "key": "test_new_asset",
              "target_audience_description": null,
              "asset_types": null
            }
          }
        },
        "structured_scopes": {
          "data": [
            {
              "id": "<id>",
              "type": "structured-scope",
              "attributes": {
                "asset_identifier": "api.example.com",
                "asset_type": "URL",
                "confidentiality_requirement": "high",
                "integrity_requirement": "high",
                "availability_requirement": "high",
                "max_severity": "critical",
                "created_at": "2025-01-01T00:00:00.000Z",
                "updated_at": "2025-01-01T00:00:00.000Z",
                "instruction": null,
                "eligible_for_bounty": true,
                "eligible_for_submission": true,
                "reference": "H001001"
              }
            }
          ]
        },
        "bounty_table_row": {
          "data": {
            "id": "<id>",
            "type": "bounty-table-row",
            "attributes": {
              "low": 500,
              "medium": 1000,
              "high": 2500,
              "critical": 5000
            }
          }
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2026-04-10

`GET /programs/{id}/campaigns`

This endpoint can be used to list all campaigns for a program. When the request is successful, the API will respond with paginated campaign objects.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create Campaign

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/campaigns" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "campaign",
    "attributes": {
      "campaign_type": "multiplier",
      "campaign_objective_id": 0,
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "bounty_pool_limit": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "campaign",
    "attributes": {
      "campaign_type": "multiplier",
      "campaign_objective_id": 0,
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "bounty_pool_limit": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/campaigns',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "campaign",
    "attributes": {
      "campaign_type": "multiplier",
      "campaign_objective_id": 0,
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "bounty_pool_limit": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/campaigns',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/campaigns");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"campaign_type\": \"multiplier\",\n      \"campaign_objective_id\": 0,\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"bounty_pool_limit\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"campaign_type\": \"multiplier\",\n      \"campaign_objective_id\": 0,\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"bounty_pool_limit\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/campaigns',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"campaign_type\": \"multiplier\",\n      \"campaign_objective_id\": 0,\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"bounty_pool_limit\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/campaigns", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaign created

```
{
  "id": "<id>",
  "type": "campaign",
  "attributes": {
    "campaign_type": "multiplier",
    "researchers_information": "Focus on authentication bypass vulnerabilities",
    "critical": 2,
    "high": 1.5,
    "medium": 1.5,
    "low": 1,
    "bounty_pool_limit": null,
    "start_date": "2026-04-01T01:00:00.000Z",
    "end_date": "2026-04-10T23:00:00.000Z",
    "status": "scheduled",
    "target_audience": false,
    "extended_at": null,
    "total_reports": 0,
    "valid_reports": 0,
    "total_critical_reports": 0,
    "total_high_reports": 0,
    "bounty_spent": 0
  },
  "relationships": {
    "campaign_objective": {
      "data": {
        "id": "<id>",
        "type": "campaign-objective",
        "attributes": {
          "name": "Test new asset",
          "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
          "category": "newest_changes",
          "key": "test_new_asset",
          "target_audience_description": null,
          "asset_types": null
        }
      }
    },
    "structured_scopes": {
      "data": [
        {
          "id": "<id>",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "URL",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2025-01-01T00:00:00.000Z",
            "updated_at": "2025-01-01T00:00:00.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      ]
    },
    "bounty_table_row": {
      "data": {
        "id": "<id>",
        "type": "bounty-table-row",
        "attributes": {
          "low": 500,
          "medium": 1000,
          "high": 2500,
          "critical": 5000
        }
      }
    }
  }
}

```

Last revised: 2026-04-10

`POST /programs/{id}/campaigns`

This endpoint can be used to create a new campaign for a program. Campaigns allow program managers to incentivize hackers by offering bounty multipliers on specific assets for a limited time.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information required to create a campaign. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» campaign_type | body | string | true | The type of campaign. |
| »» campaign_objective_id | body | integer | true | The ID of the campaign objective. |
| »» researchers_information | body | string | false | Additional information for researchers about the campaign. |
| »» critical | body | number(float) | true | The bounty multiplier for critical severity findings. Must be greater than 1.0. |
| »» high | body | number(float) | true | The bounty multiplier for high severity findings. Must be greater than 1.0. |
| »» medium | body | number(float) | false | The bounty multiplier for medium severity findings. |
| »» low | body | number(float) | false | The bounty multiplier for low severity findings. |
| »» bounty_pool_limit | body | integer¦null | false | The maximum bounty pool budget for the campaign. |
| »» start_date | body | string(date-time) | true | The start date of the campaign. Must be at least 3 days from now. |
| »» end_date | body | string(date-time) | true | The end date of the campaign. Must be at least 4 days from now. |
| »» structured_scope_ids | body | [integer] | false | The IDs of the structured scopes to associate with the campaign. If empty, all assets are targeted. |
| »» bounty_table_row_id | body | integer¦null | false | The ID of the bounty table row to associate with the campaign. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | campaign |

### Get Campaign

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaign found

```
{
  "id": "<id>",
  "type": "campaign",
  "attributes": {
    "campaign_type": "multiplier",
    "researchers_information": "Focus on authentication bypass vulnerabilities",
    "critical": 2,
    "high": 1.5,
    "medium": 1.5,
    "low": 1,
    "bounty_pool_limit": null,
    "start_date": "2026-04-01T01:00:00.000Z",
    "end_date": "2026-04-10T23:00:00.000Z",
    "status": "scheduled",
    "target_audience": false,
    "extended_at": null,
    "total_reports": 0,
    "valid_reports": 0,
    "total_critical_reports": 0,
    "total_high_reports": 0,
    "bounty_spent": 0
  },
  "relationships": {
    "campaign_objective": {
      "data": {
        "id": "<id>",
        "type": "campaign-objective",
        "attributes": {
          "name": "Test new asset",
          "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
          "category": "newest_changes",
          "key": "test_new_asset",
          "target_audience_description": null,
          "asset_types": null
        }
      }
    },
    "structured_scopes": {
      "data": [
        {
          "id": "<id>",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "URL",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2025-01-01T00:00:00.000Z",
            "updated_at": "2025-01-01T00:00:00.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      ]
    },
    "bounty_table_row": {
      "data": {
        "id": "<id>",
        "type": "bounty-table-row",
        "attributes": {
          "low": 500,
          "medium": 1000,
          "high": 2500,
          "critical": 5000
        }
      }
    }
  }
}

```

Last revised: 2026-04-10

`GET /programs/{program_id}/campaigns/{id}`

This endpoint can be used to get the details of a specific campaign.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the campaign. |

### Update Campaign

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}" \
  -X PATCH \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "campaign",
    "attributes": {
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "campaign",
    "attributes": {
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}

r = requests.patch(
  'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "campaign",
    "attributes": {
      "researchers_information": "string",
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "start_date": "2019-08-24T14:15:22Z",
      "end_date": "2019-08-24T14:15:22Z",
      "structured_scope_ids": [
        0
      ],
      "bounty_table_row_id": 0
    }
  }
}

result = RestClient::Request.execute(
  method: :patch,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PATCH");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"campaign\",\n    \"attributes\": {\n      \"researchers_information\": \"string\",\n      \"critical\": 0,\n      \"high\": 0,\n      \"medium\": 0,\n      \"low\": 0,\n      \"start_date\": \"2019-08-24T14:15:22Z\",\n      \"end_date\": \"2019-08-24T14:15:22Z\",\n      \"structured_scope_ids\": [\n        0\n      ],\n      \"bounty_table_row_id\": 0\n    }\n  }\n}"`))

    req, err := http.NewRequest("PATCH", "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaign updated

```
{
  "id": "<id>",
  "type": "campaign",
  "attributes": {
    "campaign_type": "multiplier",
    "researchers_information": "Focus on authentication bypass vulnerabilities",
    "critical": 2,
    "high": 1.5,
    "medium": 1.5,
    "low": 1,
    "bounty_pool_limit": null,
    "start_date": "2026-04-01T01:00:00.000Z",
    "end_date": "2026-04-10T23:00:00.000Z",
    "status": "scheduled",
    "target_audience": false,
    "extended_at": null,
    "total_reports": 0,
    "valid_reports": 0,
    "total_critical_reports": 0,
    "total_high_reports": 0,
    "bounty_spent": 0
  },
  "relationships": {
    "campaign_objective": {
      "data": {
        "id": "<id>",
        "type": "campaign-objective",
        "attributes": {
          "name": "Test new asset",
          "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
          "category": "newest_changes",
          "key": "test_new_asset",
          "target_audience_description": null,
          "asset_types": null
        }
      }
    },
    "structured_scopes": {
      "data": [
        {
          "id": "<id>",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "URL",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2025-01-01T00:00:00.000Z",
            "updated_at": "2025-01-01T00:00:00.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      ]
    },
    "bounty_table_row": {
      "data": {
        "id": "<id>",
        "type": "bounty-table-row",
        "attributes": {
          "low": 500,
          "medium": 1000,
          "high": 2500,
          "critical": 5000
        }
      }
    }
  }
}

```

Last revised: 2026-04-10

`PATCH /programs/{program_id}/campaigns/{id}`

This endpoint can be used to update an existing campaign. Scheduled campaigns allow updating most fields, while active campaigns can only update end_date, researchers_information, and extended_at.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the campaign. |
| data | body | object | true | The information to update a campaign. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» researchers_information | body | string | false | Additional information for researchers about the campaign. |
| »» critical | body | number(float) | false | The bounty multiplier for critical severity findings. |
| »» high | body | number(float) | false | The bounty multiplier for high severity findings. |
| »» medium | body | number(float) | false | The bounty multiplier for medium severity findings. |
| »» low | body | number(float) | false | The bounty multiplier for low severity findings. |
| »» start_date | body | string(date-time) | true | The start date of the campaign. |
| »» end_date | body | string(date-time) | true | The end date of the campaign. |
| »» structured_scope_ids | body | [integer] | false | The IDs of the structured scopes to associate with the campaign. |
| »» bounty_table_row_id | body | integer¦null | false | The ID of the bounty table row to associate with the campaign. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | campaign |

### Launch Campaign

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/launch", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaign launched

```
{
  "id": "<id>",
  "type": "campaign",
  "attributes": {
    "campaign_type": "multiplier",
    "researchers_information": "Focus on authentication bypass vulnerabilities",
    "critical": 2,
    "high": 1.5,
    "medium": 1.5,
    "low": 1,
    "bounty_pool_limit": null,
    "start_date": "2026-04-01T01:00:00.000Z",
    "end_date": "2026-04-10T23:00:00.000Z",
    "status": "scheduled",
    "target_audience": false,
    "extended_at": null,
    "total_reports": 0,
    "valid_reports": 0,
    "total_critical_reports": 0,
    "total_high_reports": 0,
    "bounty_spent": 0
  },
  "relationships": {
    "campaign_objective": {
      "data": {
        "id": "<id>",
        "type": "campaign-objective",
        "attributes": {
          "name": "Test new asset",
          "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
          "category": "newest_changes",
          "key": "test_new_asset",
          "target_audience_description": null,
          "asset_types": null
        }
      }
    },
    "structured_scopes": {
      "data": [
        {
          "id": "<id>",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "URL",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2025-01-01T00:00:00.000Z",
            "updated_at": "2025-01-01T00:00:00.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      ]
    },
    "bounty_table_row": {
      "data": {
        "id": "<id>",
        "type": "bounty-table-row",
        "attributes": {
          "low": 500,
          "medium": 1000,
          "high": 2500,
          "critical": 5000
        }
      }
    }
  }
}

```

Last revised: 2026-04-10

`POST /programs/{program_id}/campaigns/{id}/launch`

This endpoint can be used to launch a scheduled campaign, transitioning it from "scheduled" to "active" status.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the campaign to launch. |

### End Campaign Prematurely

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{program_id}/campaigns/{id}/end_prematurely", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

campaign ended prematurely

```
{
  "id": "<id>",
  "type": "campaign",
  "attributes": {
    "campaign_type": "multiplier",
    "researchers_information": "Focus on authentication bypass vulnerabilities",
    "critical": 2,
    "high": 1.5,
    "medium": 1.5,
    "low": 1,
    "bounty_pool_limit": null,
    "start_date": "2026-04-01T01:00:00.000Z",
    "end_date": "2026-04-10T23:00:00.000Z",
    "status": "scheduled",
    "target_audience": false,
    "extended_at": null,
    "total_reports": 0,
    "valid_reports": 0,
    "total_critical_reports": 0,
    "total_high_reports": 0,
    "bounty_spent": 0
  },
  "relationships": {
    "campaign_objective": {
      "data": {
        "id": "<id>",
        "type": "campaign-objective",
        "attributes": {
          "name": "Test new asset",
          "description": "Test if your assets are ready before exposing to a wider audience of researchers.",
          "category": "newest_changes",
          "key": "test_new_asset",
          "target_audience_description": null,
          "asset_types": null
        }
      }
    },
    "structured_scopes": {
      "data": [
        {
          "id": "<id>",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "URL",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2025-01-01T00:00:00.000Z",
            "updated_at": "2025-01-01T00:00:00.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      ]
    },
    "bounty_table_row": {
      "data": {
        "id": "<id>",
        "type": "bounty-table-row",
        "attributes": {
          "low": 500,
          "medium": 1000,
          "high": 2500,
          "critical": 5000
        }
      }
    }
  }
}

```

Last revised: 2026-04-10

`POST /programs/{program_id}/campaigns/{id}/end_prematurely`

This endpoint can be used to end an active campaign prematurely. The campaign's end date will be set to tomorrow and hackers will be notified.

The campaign must be active and not already ending within 3 days.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the campaign to end. |

### Get Common Responses

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/common_responses" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/common_responses',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/common_responses',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/common_responses");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/common_responses',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/common_responses", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

reporters found

```
{
  "data": [
    {
      "id": "108878",
      "attributes": {
        "title": "Vulnerability Scanner False Positive",
        "message": "Automated vulnerability scanners commonly have low priority issues and/or false positives. Before submitting the results from a scanner, please take a moment to confirm that the reported issues are actually valid and exploitable. Please reply if you have a working proof-of-concept or reason to believe that this issue is exploitable.\n"
      }
    },
    {
      "id": "108886",
      "attributes": {
        "title": "X-XSS-Protection",
        "message": "Automated vulnerability scanners commonly have low priority issues and/or false positives. Before submitting the results from a scanner, please take a moment to confirm that the reported issues are actually valid and exploitable. In this specific case, we believe that the default state of the `X-XSS-Protection` header is sufficient for our purposes. Please reply if you have a working proof-of-concept that could be mitigated by an adjustment to our header.\n"
      }
    },
    {
      "id": "108891",
      "attributes": {
        "title": "Video Without Content",
        "message": "Using a video to demonstrate a potential issue should only be necessary in rare situations and should always be accompanied with a text description of the issue as well. Please update this report with step-by-step instructions to reproduce the core components of the issue. If you don't speak English, feel free to leave your report in your own language, and we'll try our best to find someone who can help translate.\n"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/common_responses`

Common responses can be fetched by sending a GET request to the common responses endpoint. When the request is successful, the API will respond with paginated common responses.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create a CVE Request

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/cve_requests" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "cve-request",
    "attributes": {
      "team_handle": "string",
      "versions": [
        {
          "vendor": "string",
          "product": "string",
          "func": "string",
          "version": "string",
          "versionUpperBound": "string",
          "versionType": "string",
          "affected": true
        }
      ],
      "metrics": [
        {
          "vectorString": "string"
        }
      ],
      "weakness_id": 0,
      "description": "string",
      "vulnerability_discovered_at": "2019-08-24T14:15:22Z"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "cve-request",
    "attributes": {
      "team_handle": "string",
      "versions": [
        {
          "vendor": "string",
          "product": "string",
          "func": "string",
          "version": "string",
          "versionUpperBound": "string",
          "versionType": "string",
          "affected": true
        }
      ],
      "metrics": [
        {
          "vectorString": "string"
        }
      ],
      "weakness_id": 0,
      "description": "string",
      "vulnerability_discovered_at": "2019-08-24T14:15:22Z"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/cve_requests',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "cve-request",
    "attributes": {
      "team_handle": "string",
      "versions": [
        {
          "vendor": "string",
          "product": "string",
          "func": "string",
          "version": "string",
          "versionUpperBound": "string",
          "versionType": "string",
          "affected": true
        }
      ],
      "metrics": [
        {
          "vectorString": "string"
        }
      ],
      "weakness_id": 0,
      "description": "string",
      "vulnerability_discovered_at": "2019-08-24T14:15:22Z"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/cve_requests',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/cve_requests");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"cve-request\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"versions\": [\n        {\n          \"vendor\": \"string\",\n          \"product\": \"string\",\n          \"func\": \"string\",\n          \"version\": \"string\",\n          \"versionUpperBound\": \"string\",\n          \"versionType\": \"string\",\n          \"affected\": true\n        }\n      ],\n      \"metrics\": [\n        {\n          \"vectorString\": \"string\"\n        }\n      ],\n      \"weakness_id\": 0,\n      \"description\": \"string\",\n      \"vulnerability_discovered_at\": \"2019-08-24T14:15:22Z\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"cve-request\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"versions\": [\n        {\n          \"vendor\": \"string\",\n          \"product\": \"string\",\n          \"func\": \"string\",\n          \"version\": \"string\",\n          \"versionUpperBound\": \"string\",\n          \"versionType\": \"string\",\n          \"affected\": true\n        }\n      ],\n      \"metrics\": [\n        {\n          \"vectorString\": \"string\"\n        }\n      ],\n      \"weakness_id\": 0,\n      \"description\": \"string\",\n      \"vulnerability_discovered_at\": \"2019-08-24T14:15:22Z\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/cve_requests',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"cve-request\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"versions\": [\n        {\n          \"vendor\": \"string\",\n          \"product\": \"string\",\n          \"func\": \"string\",\n          \"version\": \"string\",\n          \"versionUpperBound\": \"string\",\n          \"versionType\": \"string\",\n          \"affected\": true\n        }\n      ],\n      \"metrics\": [\n        {\n          \"vectorString\": \"string\"\n        }\n      ],\n      \"weakness_id\": 0,\n      \"description\": \"string\",\n      \"vulnerability_discovered_at\": \"2019-08-24T14:15:22Z\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/cve_requests", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

CVE request created

```
{
  "id": "1337",
  "type": "cve-request",
  "attributes": {
    "request_type": "new",
    "versions": [
      {
        "func": "<",
        "vendor": "WidgetFactory",
        "product": "WidgetOne",
        "version": "1.0.0",
        "versionUpperBound": "2.0.0",
        "affected": true,
        "versionType": "semver"
      }
    ],
    "metrics": [
      {
        "vectorString": "CVSS:3.0/AV:A/AC:H/PR:L/UI:R/S:C/C:N/I:L/A:N"
      }
    ],
    "products": [
      "WidgetFactory WidgetOne"
    ],
    "description": "Insufficient URI encoding in WidgetOne before 1.0.0 allows attacker to inject arbitrary parameters into API requests.",
    "references": [],
    "report_id": null,
    "team_handle": "acme",
    "state": "draft",
    "vulnerability_discovered_at": "2024-01-20",
    "created_at": "2024-01-20T14:26:19.286Z",
    "updated_at": "2024-01-20T14:26:19.286Z",
    "weakness_name": "Improper Input Validation",
    "latest_state_change_reason": null,
    "cve_identifier": null,
    "auto_submit_on_publicly_disclosing_report": true
  }
}

```

Last revised: 2026-03-26

`POST /programs/{id}/cve_requests`

This API endpoint can be used to create a new CVE request. When the API call is successful, a [cve_request object](https://api.hackerone.com/customer-reference#cve_request) will be returned.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information to be requested from the hacker. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» team_handle | body | string | true | The handle of the team. |
| »» versions | body | [object] | true | none |
| »»» vendor | body | string | true | The vendor of the version. |
| »»» product | body | string | true | The product of the version. |
| »»» func | body | string | true | The function of the version. |
| »»» version | body | string | true | The version. |
| »»» versionUpperBound | body | string | false | The upper bound version. Optional field that specifies the end of a version range. If not provided or empty, defaults to the value of 'version'. |
| »»» versionType | body | string | true | The type of the version. |
| »»» affected | body | boolean | true | Whether the version is affected or not. |
| »» metrics | body | [object] | true | none |
| »»» vectorString | body | string | true | The vector string. |
| »» weakness_id | body | integer | true | The ID of the weakness. |
| »» description | body | string | true | A description of the information required from the hackers to create a CVE request. |
| »» vulnerability_discovered_at | body | string(date-time) | true | The date when the vulnerability was discovered. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | cve-request |

### Get all CVE Requests

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/cve_requests" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/cve_requests',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/cve_requests',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/cve_requests");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/cve_requests',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/cve_requests", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

CVE requests listed

```
{
  "id": "1337",
  "type": "cve-request",
  "attributes": {
    "request_type": "new",
    "versions": [
      {
        "func": "<",
        "vendor": "WidgetFactory",
        "product": "WidgetOne",
        "version": "1.0.0",
        "versionUpperBound": "2.0.0",
        "affected": true,
        "versionType": "semver"
      }
    ],
    "metrics": [
      {
        "vectorString": "CVSS:3.0/AV:A/AC:H/PR:L/UI:R/S:C/C:N/I:L/A:N"
      }
    ],
    "products": [
      "WidgetFactory WidgetOne"
    ],
    "description": "Insufficient URI encoding in WidgetOne before 1.0.0 allows attacker to inject arbitrary parameters into API requests.",
    "references": [],
    "report_id": null,
    "team_handle": "acme",
    "state": "draft",
    "vulnerability_discovered_at": "2024-01-20",
    "created_at": "2024-01-20T14:26:19.286Z",
    "updated_at": "2024-01-20T14:26:19.286Z",
    "weakness_name": "Improper Input Validation",
    "latest_state_change_reason": null,
    "cve_identifier": null,
    "auto_submit_on_publicly_disclosing_report": true
  }
}

```

Last revised: 2026-03-26

`GET /programs/{id}/cve_requests`

This API endpoint can be used to list all the CVE requests for a program. When the API call is successful, a list of [cve_request objects](https://api.hackerone.com/customer-reference#cve_request) will be returned.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Get Hacker Invitations

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/hacker_invitations" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/hacker_invitations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/hacker_invitations", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

hacker invitations found

```
{
  "data": [
    {
      "id": "123",
      "type": "invitation-hacker",
      "attributes": {
        "state": "accepted",
        "created_at": "2024-02-02T04:05:06.000Z",
        "viewed_at": "2024-02-02T08:05:06.000Z",
        "accepted_at": "2024-03-02T04:05:06.000Z",
        "expires_at": null,
        "updated_at": "2024-03-02T04:05:06.000Z",
        "rejected_at": null,
        "cancelled_at": null
      },
      "relationships": {
        "recipient": {
          "id": "2",
          "type": "user",
          "attributes": {
            "username": "api-example 2",
            "name": "API Example 2",
            "disabled": false,
            "created_at": "2022-02-02T08:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            },
            "signal": null,
            "impact": null,
            "reputation": null,
            "bio": "Super great hacker",
            "website": "http://hackerone.com",
            "location": "Who wants to know?",
            "hackerone_triager": false
          }
        },
        "invited_by": {
          "id": "1",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2020-02-02T08:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            },
            "signal": 7,
            "impact": 30,
            "reputation": 7,
            "bio": "Super great hacker",
            "website": "http://hackerone.com",
            "location": "Who wants to know?",
            "hackerone_triager": false
          }
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2026-01-29

`GET /programs/{id}/hacker_invitations`

This resource allows you to retrieve a list of invitations to your private program.

Multiple hacker invitations objects can be queried by sending a GET request to the hacker invitations endpoint. When the request is successful, the API will respond with paginated [hacker invitations objects](https://api.hackerone.com/customer-reference#invitation-hacker).

Required permissions: Program Member. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Invite Hackers to Program

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/hacker_invitations" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "hacker-invitation",
    "attributes": {
      "usernames": [
        "string"
      ],
      "email_addresses": [
        "string"
      ],
      "message": "string",
      "context": "string",
      "bcc_me": false
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "hacker-invitation",
    "attributes": {
      "usernames": [
        "string"
      ],
      "email_addresses": [
        "string"
      ],
      "message": "string",
      "context": "string",
      "bcc_me": false
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "hacker-invitation",
    "attributes": {
      "usernames": [
        "string"
      ],
      "email_addresses": [
        "string"
      ],
      "message": "string",
      "context": "string",
      "bcc_me": false
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/hacker_invitations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"hacker-invitation\",\n    \"attributes\": {\n      \"usernames\": [\n        \"string\"\n      ],\n      \"email_addresses\": [\n        \"string\"\n      ],\n      \"message\": \"string\",\n      \"context\": \"string\",\n      \"bcc_me\": false\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"hacker-invitation\",\n    \"attributes\": {\n      \"usernames\": [\n        \"string\"\n      ],\n      \"email_addresses\": [\n        \"string\"\n      ],\n      \"message\": \"string\",\n      \"context\": \"string\",\n      \"bcc_me\": false\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/hacker_invitations',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"hacker-invitation\",\n    \"attributes\": {\n      \"usernames\": [\n        \"string\"\n      ],\n      \"email_addresses\": [\n        \"string\"\n      ],\n      \"message\": \"string\",\n      \"context\": \"string\",\n      \"bcc_me\": false\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/hacker_invitations", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

hackers invited

```
{
  "data": {
    "type": "hacker-invitation-result",
    "attributes": {
      "users_validation_result": [
        {
          "table": {
            "user": "jane",
            "username": "jane",
            "email": null,
            "reasons": []
          }
        }
      ]
    }
  }
}

```

Last revised: 2026-01-29

`POST /programs/{id}/hacker_invitations`

This endpoint allows you to invite hackers to your private program by username or email address.

When the API request is successful, the endpoint will return a validation result showing which users were successfully invited and which failed validation (e.g., user not found, already invited, banned, etc.).

Required permissions: Program Management. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The hacker invitation request details |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» usernames | body | [string] | false | Array of HackerOne usernames to invite |
| »» email_addresses | body | [string] | false | Array of email addresses to invite |
| »» message | body | string | true | Personal message to include in the invitation email |
| »» context | body | string | true | Context for the invitation (e.g., "Just getting started", "Hacker has a ready submission") |
| »» bcc_me | body | boolean | false | Whether to BCC the invitation sender on emails |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | hacker-invitation |

### Get Program Members

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/members" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/members',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/members',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/members");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/members',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/members", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

program members found

```
{
  "data": [
    {
      "id": "1",
      "type": "organization-member",
      "attributes": {
        "created_at": "2024-01-15T10:30:00.000Z",
        "organization_admin": false
      },
      "relationships": {
        "user": {
          "data": {
            "id": "101",
            "type": "user",
            "attributes": {
              "username": "john_doe",
              "name": "John Doe",
              "disabled": false,
              "created_at": "2023-06-01T08:00:00.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "organization_member_groups": {
          "data": [
            {
              "id": "201",
              "type": "organization-member-group",
              "attributes": {
                "name": "Program Managers",
                "permissions": [
                  "report_analyst",
                  "program_admin"
                ]
              }
            }
          ]
        }
      }
    },
    {
      "id": "2",
      "type": "organization-member",
      "attributes": {
        "created_at": "2024-02-20T14:45:00.000Z",
        "organization_admin": true
      },
      "relationships": {
        "user": {
          "data": {
            "id": "102",
            "type": "user",
            "attributes": {
              "username": "jane_smith",
              "name": "Jane Smith",
              "disabled": false,
              "created_at": "2023-08-15T12:30:00.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "organization_member_groups": {
          "data": [
            {
              "id": "201",
              "type": "organization-member-group",
              "attributes": {
                "name": "Program Managers",
                "permissions": [
                  "report_analyst",
                  "program_admin"
                ]
              }
            },
            {
              "id": "202",
              "type": "organization-member-group",
              "attributes": {
                "name": "Administrators",
                "permissions": [
                  "organization_admin"
                ]
              }
            }
          ]
        }
      }
    }
  ],
  "links": {
    "first": "https://api.hackerone.com/v1/programs/1234/members?page[number]=1&page[size]=25",
    "next": "https://api.hackerone.com/v1/programs/1234/members?page[number]=2&page[size]=25"
  }
}

```

Last revised: 2025-10-31

`GET /programs/{id}/members`

This endpoint allows you to retrieve a list of organization members who have access to a specific program.

The endpoint returns organization members who are associated with the program through organization member groups. By default, all users including system users are returned.

Multiple member objects can be queried by sending a GET request to this endpoint. When the request is successful, the API will respond with paginated [organization member objects](https://api.hackerone.com/customer-reference#organization-member).

Pagination: This endpoint supports cursor-based pagination and returns a maximum of 100 results per page.

Filtering: You can exclude system users by passing`filter[exclude_system_users]=true` as a query parameter.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| filter[exclude_system_users] | query | boolean | false | Set to true to exclude system users from the results. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Notify External Platform

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/notify_external_platform" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "notify-external-platform",
    "attributes": {
      "message": "string",
      "targets": [
        "string"
      ],
      "integration_id": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "notify-external-platform",
    "attributes": {
      "message": "string",
      "targets": [
        "string"
      ],
      "integration_id": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/notify_external_platform',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "notify-external-platform",
    "attributes": {
      "message": "string",
      "targets": [
        "string"
      ],
      "integration_id": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/notify_external_platform',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/notify_external_platform");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"notify-external-platform\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"targets\": [\n        \"string\"\n      ],\n      \"integration_id\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"notify-external-platform\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"targets\": [\n        \"string\"\n      ],\n      \"integration_id\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/notify_external_platform',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"notify-external-platform\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"targets\": [\n        \"string\"\n      ],\n      \"integration_id\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/notify_external_platform", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Notify External Platform

```
{
  "data": {
    "was_successful": true
  }
}

```

400 Response

```
{
  "errors": [
    {
      "status": 0,
      "title": "string",
      "detail": "string"
    }
  ]
}

```

Last revised: 2025-10-14

`POST /programs/{id}/notify_external_platform`

Use your integration to send a custom message to an external platform (e.g. Slack). For Slack, targets can be channel names (e.g., "general", "security") or channel IDs (e.g., "C1234567890").

Required permission: Report Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information to send a message to an external platform. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» message | body | string | true | The message to be sent to the external platform. Maximum length is 10,000 characters. |
| »» targets | body | [string] | true | Array of target channels/users to send the message to. Maximum is 25 targets. |
| »» integration_id | body | string | true | The ID of the integration/solution instance to use. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | notify-external-platform |

### Upload Policy Attachments

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/policy_attachments" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -d @- <<EOD
null
EOD

```

```
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

data = null

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/policy_attachments',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

data = null

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/policy_attachments',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/policy_attachments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "null";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "null";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'multipart/form-data');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/policy_attachments',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"null"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/policy_attachments", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

attachment uploaded

```
{
  "id": "1337",
  "type": "attachment",
  "attributes": {
    "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
    "created_at": "2016-02-02T04:05:06.000Z",
    "file_name": "root.rb",
    "content_type": "text/x-ruby",
    "file_size": 2871
  }
}

```

Last revised: 2025-10-23

`POST /programs/{id}/policy_attachments`

Policy attachments can be uploaded by sending a POST request to the program policy attachments endpoint. When the API call is successful, an [attachment](https://api.hackerone.com/customer-reference#attachment) object will be returned.

You can use the attachment ID to display the attachment on your policy page. For example, if the attachment ID is`1337`, then include`{F1337}` in your policy to display the attachment.

File Validation Requirements: - Maximum file size: 250 MB - Maximum filename length: 255 characters - GIF images: Maximum dimensions 1920x1080 pixels

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Update Policy

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/policy" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "program-policy",
    "attributes": {
      "policy": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "program-policy",
    "attributes": {
      "policy": "string"
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/programs/{id}/policy',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "program-policy",
    "attributes": {
      "policy": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/programs/{id}/policy',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/policy");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"program-policy\",\n    \"attributes\": {\n      \"policy\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"program-policy\",\n    \"attributes\": {\n      \"policy\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/policy',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"program-policy\",\n    \"attributes\": {\n      \"policy\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/programs/{id}/policy", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Policy updated

```
{
  "data": {
    "id": "12",
    "type": "program",
    "attributes": {
      "handle": "security",
      "policy": "...",
      "created_at": "2013-01-01T00:00:00.000Z",
      "updated_at": "2019-08-26T13:53:24.807Z"
    }
  }
}

```

Last revised: 2025-05-23

`PUT /programs/{id}/policy`

Managing the policy of a program through the HackerOne API can be useful to programmatically batch update programs in HackerOne. You can use this endpoint to update the policy of your program.

Required permissions: Program Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information to update the policy of a program. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» policy | body | string | true | The new policy that will be set on the program. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | program-policy |

### Get Reporters

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/reporters" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/reporters',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/reporters',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/reporters");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/reporters',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/reporters", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

reporters found

```
{
  "data": [
    {
      "id": "1337",
      "type": "user",
      "attributes": {
        "username": "awesome-hacker",
        "name": "Awesome Hacker",
        "disabled": false,
        "created_at": "2016-02-02T04:05:06.000Z",
        "profile_picture": {
          "62x62": "/assets/avatars/default.png",
          "82x82": "/assets/avatars/default.png",
          "110x110": "/assets/avatars/default.png",
          "260x260": "/assets/avatars/default.png"
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/reporters`

This resource allows you to retrieve a list of all users that ever submitted a report to the program.

Multiple user objects can be queried by sending a GET request to the reporters endpoint. When the request is successful, the API will respond with paginated [user objects](https://api.hackerone.com/customer-reference#user).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Scope Exclusions

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/scope_exclusions" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/scope_exclusions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/scope_exclusions", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

scope exclusions found

```
{
  "data": [
    {
      "id": "123",
      "type": "scope-exclusion",
      "attributes": {
        "category": "Custom exclusion name",
        "details": "Description of what is excluded",
        "created_at": "2024-01-01T00:00:00.000Z",
        "updated_at": "2024-01-01T00:00:00.000Z"
      }
    }
  ]
}

```

Last revised: 2026-04-22

`GET /programs/{id}/scope_exclusions`

Scope exclusions can be fetched by sending a GET request to the scope exclusions endpoint. When the request is successful, the API will respond with a list of [scope exclusion objects](https://api.hackerone.com/customer-reference#scope-exclusion).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Create Scope Exclusion

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/scope_exclusions" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/scope_exclusions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/scope_exclusions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/scope_exclusions", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

scope exclusion created

```
{
  "data": {
    "id": "123",
    "type": "scope-exclusion",
    "attributes": {
      "category": "Custom exclusion name",
      "details": "Description of what is excluded",
      "created_at": "2024-01-01T00:00:00.000Z",
      "updated_at": "2024-01-01T00:00:00.000Z"
    }
  }
}

```

Last revised: 2026-04-22

`POST /programs/{id}/scope_exclusions`

Use this endpoint to create a scope exclusion for a program. When the API call is successful, a [scope exclusion](https://api.hackerone.com/customer-reference#scope-exclusion) object will be returned.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information required to create a scope exclusion. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» category | body | string | false | The category name for the scope exclusion (max 100 characters). |
| »» details | body | string | false | Description of what is excluded from the program scope (max 300 characters). |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | scope-exclusion |

### Update Scope Exclusion

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "scope-exclusion",
    "attributes": {
      "category": "string",
      "details": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"scope-exclusion\",\n    \"attributes\": {\n      \"category\": \"string\",\n      \"details\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

scope exclusion updated

```
{
  "data": {
    "id": "123",
    "type": "scope-exclusion",
    "attributes": {
      "category": "Updated exclusion name",
      "details": "Updated description",
      "created_at": "2024-01-01T00:00:00.000Z",
      "updated_at": "2024-01-01T00:00:00.000Z"
    }
  }
}

```

Last revised: 2026-04-22

`PUT /programs/{program_id}/scope_exclusions/{id}`

Use this endpoint to update a scope exclusion for a program. When the API call is successful, the updated [scope exclusion](https://api.hackerone.com/customer-reference#scope-exclusion) object will be returned.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the scope exclusion. |
| data | body | object | true | The information required to update a scope exclusion. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» category | body | string | false | The category name for the scope exclusion (max 100 characters). |
| »» details | body | string | false | Description of what is excluded from the program scope (max 300 characters). |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | scope-exclusion |

### Delete Scope Exclusion

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>"

```

```
import requests

r = requests.delete(
  'https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>')
)

print(r.json())

```

```
require 'rest-client'
require 'json'

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>'
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));

fetch('https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}',
{
  method: 'DELETE'

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/programs/{program_id}/scope_exclusions/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Last revised: 2026-04-22

`DELETE /programs/{program_id}/scope_exclusions/{id}`

Use this endpoint to delete a scope exclusion from a program.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the scope exclusion. |

### Get Structured Scopes

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/structured_scopes" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/structured_scopes',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/structured_scopes',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/structured_scopes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/structured_scopes',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/structured_scopes", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

structured scopes found

```
{
  "data": [
    {
      "id": "57",
      "type": "structured-scope",
      "attributes": {
        "asset_identifier": "api.example.com",
        "asset_type": "URL",
        "confidentiality_requirement": "high",
        "integrity_requirement": "high",
        "availability_requirement": "high",
        "max_severity": "critical",
        "created_at": "2015-02-02T04:05:06.000Z",
        "updated_at": "2016-05-02T04:05:06.000Z",
        "instruction": null,
        "eligible_for_bounty": true,
        "eligible_for_submission": true,
        "reference": "H001001"
      }
    },
    {
      "id": "58",
      "type": "structured-scope",
      "attributes": {
        "asset_identifier": "www.example.com",
        "asset_type": "URL",
        "confidentiality_requirement": "low",
        "integrity_requirement": "high",
        "availability_requirement": "high",
        "max_severity": "critical",
        "created_at": "2017-02-03T04:05:10.000Z",
        "updated_at": "2018-05-02T04:05:10.000Z",
        "instruction": "Instruction text",
        "eligible_for_bounty": true,
        "eligible_for_submission": true,
        "reference": "H001002"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2026-04-07

`GET /programs/{id}/structured_scopes`

Structured scopes can be fetched by sending a GET request to the structured scopes endpoint. When the request is successful, the API will respond with paginated [structured scope objects](https://api.hackerone.com/customer-reference#structured-scope).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. You can find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs). |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Awarded Swag

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/swag" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/swag',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/swag',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/swag");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/swag',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/swag", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

swag found

```
{
  "data": [
    {
      "id": "8",
      "type": "swag",
      "attributes": {
        "sent": true,
        "created_at": "2019-08-30T08:33:42.147Z"
      },
      "relationships": {
        "user": {
          "data": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "address": {
          "data": {
            "id": "1337",
            "type": "address",
            "attributes": {
              "name": "Jane Doe",
              "street": "535 Mission Street",
              "city": "San Francisco",
              "postal_code": "94105",
              "state": "CA",
              "country": "United States of America",
              "created_at": "2016-02-02T04:05:06.000Z",
              "tshirt_size": "M_Large",
              "phone_number": "+1-510-000-0000"
            }
          }
        }
      }
    },
    {
      "id": "7",
      "type": "swag",
      "attributes": {
        "sent": false,
        "created_at": "2019-08-20T03:47:04.163Z"
      },
      "relationships": {
        "user": {
          "data": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "johndoe",
              "name": "John Doe",
              "disabled": false,
              "created_at": "2017-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "address": {
          "data": {
            "id": "1337",
            "type": "address",
            "attributes": {
              "name": "John Smith",
              "street": "535 Mission Street",
              "city": "New York",
              "postal_code": "10001",
              "state": "NY",
              "country": "United States of America",
              "created_at": "2017-01-03T07:08:09.000Z",
              "tshirt_size": "M_Large",
              "phone_number": "+1-212-000-0000"
            }
          }
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/swag`

Awarded swag can be fetched by sending a GET request to the swag endpoint. When the request is successful, the API will respond with paginated [swag objects](https://api.hackerone.com/customer-reference#swag).

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Mark Swag as Sent

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{program_id}/swag/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {}

r = requests.put(
  'https://api.hackerone.com/v1/programs/{program_id}/swag/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/programs/{program_id}/swag/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{program_id}/swag/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{program_id}/swag/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/programs/{program_id}/swag/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Swag marked as sent

```
{
  "data": {
    "id": "8",
    "type": "swag",
    "attributes": {
      "sent": true,
      "created_at": "2019-08-30T08:33:42.147Z"
    },
    "relationships": {
      "user": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "address": {
        "data": {
          "id": "1337",
          "type": "address",
          "attributes": {
            "name": "Jane Doe",
            "street": "535 Mission Street",
            "city": "San Francisco",
            "postal_code": "94105",
            "state": "CA",
            "country": "United States of America",
            "created_at": "2016-02-02T04:05:06.000Z",
            "tshirt_size": "M_Large",
            "phone_number": "+1-510-000-0000"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`PUT /programs/{program_id}/swag/{id}`

The status of swag can be updated to "sent" through this endpoint. When the request is successful, the API will respond with a [swag object](https://api.hackerone.com/customer-reference#swag).

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| program_id | path | integer | true | The ID of the program. |
| id | path | integer | true | The ID of the swag. |

### Send Messages to Hackers

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/team_messages" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "team-message",
    "attributes": {
      "message": "Hello hackers! This is an important announcement.",
      "subject": "Important Announcement",
      "reply_to_address": "example@hackerone.com",
      "send_me_copy": true,
      "recipients": "hacker1,hacker2,hacker3",
      "message_invited_hackers": true,
      "message_top_hackers": true,
      "message_participating_hackers": true,
      "message_bounty_claimed_hackers": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "team-message",
    "attributes": {
      "message": "Hello hackers! This is an important announcement.",
      "subject": "Important Announcement",
      "reply_to_address": "example@hackerone.com",
      "send_me_copy": true,
      "recipients": "hacker1,hacker2,hacker3",
      "message_invited_hackers": true,
      "message_top_hackers": true,
      "message_participating_hackers": true,
      "message_bounty_claimed_hackers": true
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/programs/{id}/team_messages',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "team-message",
    "attributes": {
      "message": "Hello hackers! This is an important announcement.",
      "subject": "Important Announcement",
      "reply_to_address": "example@hackerone.com",
      "send_me_copy": true,
      "recipients": "hacker1,hacker2,hacker3",
      "message_invited_hackers": true,
      "message_top_hackers": true,
      "message_participating_hackers": true,
      "message_bounty_claimed_hackers": true
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/programs/{id}/team_messages',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/team_messages");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"team-message\",\n    \"attributes\": {\n      \"message\": \"Hello hackers! This is an important announcement.\",\n      \"subject\": \"Important Announcement\",\n      \"reply_to_address\": \"example@hackerone.com\",\n      \"send_me_copy\": true,\n      \"recipients\": \"hacker1,hacker2,hacker3\",\n      \"message_invited_hackers\": true,\n      \"message_top_hackers\": true,\n      \"message_participating_hackers\": true,\n      \"message_bounty_claimed_hackers\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"team-message\",\n    \"attributes\": {\n      \"message\": \"Hello hackers! This is an important announcement.\",\n      \"subject\": \"Important Announcement\",\n      \"reply_to_address\": \"example@hackerone.com\",\n      \"send_me_copy\": true,\n      \"recipients\": \"hacker1,hacker2,hacker3\",\n      \"message_invited_hackers\": true,\n      \"message_top_hackers\": true,\n      \"message_participating_hackers\": true,\n      \"message_bounty_claimed_hackers\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/team_messages',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"team-message\",\n    \"attributes\": {\n      \"message\": \"Hello hackers! This is an important announcement.\",\n      \"subject\": \"Important Announcement\",\n      \"reply_to_address\": \"example@hackerone.com\",\n      \"send_me_copy\": true,\n      \"recipients\": \"hacker1,hacker2,hacker3\",\n      \"message_invited_hackers\": true,\n      \"message_top_hackers\": true,\n      \"message_participating_hackers\": true,\n      \"message_bounty_claimed_hackers\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/programs/{id}/team_messages", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Message successfully sent

```
{
  "id": "12345",
  "type": "team-message",
  "attributes": {
    "state": "sent",
    "created_at": "2025-02-02T14:31:22.000Z"
  }
}

```

Last revised: 2025-07-21

`POST /programs/{id}/team_messages`

Use this endpoint to send messages to hackers in your program. You can target different groups of hackers based on their participation in the program.

Recipients can be specified by their usernames, or you can choose to send messages to all invited hackers, top hackers, participating hackers, or those who have claimed a bounty. At least one recipients option must be selected.

Required permissions: Program Management. You can manage the permissions of your API users through your organization's settings.

Required features: Hacker Messaging. This feature must be enabled for your program. Insufficient permissions or disabled features will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| data | body | object | true | The information required to send a message. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» message | body | string | true | The content of the message to send to hackers. This field is required. Maximum length is 5000 characters. |
| »» subject | body | string | false | The subject of the message (optional). |
| »» reply_to_address | body | string | false | Email address that hackers can use to reply to the message (optional). Must be a valid email address. |
| »» send_me_copy | body | boolean | false | Whether to send a copy of the message to the sender. |
| »» recipients | body | string | false | Comma-separated list of usernames to send the message to. Usernames must be valid HackerOne usernames. |
| »» message_invited_hackers | body | boolean | false | Send to all invited hackers. |
| »» message_top_hackers | body | boolean | false | Send to top 20 hackers in the program. |
| »» message_participating_hackers | body | boolean | false | Send to all hackers who submitted a vulnerability. |
| »» message_bounty_claimed_hackers | body | boolean | false | Send to all hackers who received a bounty. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | team-message |

### Get Thanks to Hackers

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/thanks" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/thanks',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/thanks',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/thanks");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/thanks',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/thanks", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

thanks items found

```
{
  "data": [
    {
      "type": "thanks-item",
      "attributes": {
        "total_report_count": 1,
        "reputation": 7,
        "recognized_report_count": 1,
        "username": "lorem",
        "user_id": "55"
      }
    },
    {
      "type": "thanks-item",
      "attributes": {
        "total_report_count": 1,
        "reputation": 22,
        "recognized_report_count": 1,
        "username": "ipsum",
        "user_id": "56"
      }
    },
    {
      "type": "thanks-item",
      "attributes": {
        "total_report_count": 5,
        "reputation": 38,
        "recognized_report_count": 3,
        "username": "adam",
        "user_id": "57"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/thanks`

This endpoint enables you to view a program's thanks to hackers.

A program's thanks items can be fetched by sending a GET request to the thanks endpoint. When the request is successful, the API will respond with paginated thanks items objects.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Integrations

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/integrations" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/integrations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/integrations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/integrations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/integrations',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/integrations", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Integrations found

```
{
  "data": [
    {
      "id": "Z2lkOi8vaGFja2Vyb25lL1RlYW1JbnRlZ3Jh",
      "name": "Slack integration",
      "group_type": "notification"
    },
    {
      "id": "Z2lkOi8vaGsdXRpb25JbnNZiMS0yNDQxNjgxZDVjZTQlM0Ez",
      "name": "Nnamdi Jira Integration",
      "group_type": "issue_tracking"
    },
    {
      "id": "Z2lkOi8vaGFja2Vyb25lL1RlYW1JbnRlZ3Jh",
      "name": "Manual integration",
      "group_type": "manual"
    }
  ]
}

```

Last revised: 2025-05-23

`GET /programs/{id}/integrations`

Fetch all integrations associated to a programs.

Required permission: Report Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |

### Get Triage Reviews

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/triage_reviews" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/triage_reviews',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/triage_reviews',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/triage_reviews");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/triage_reviews',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/triage_reviews", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

triage reviews found

```
{
  "data": [
    {
      "id": "1234",
      "type": "triage-review",
      "attributes": {
        "comment": "Great job!",
        "rating": 5
      },
      "relationships": {
        "user": {
          "data": {
            "id": "77",
            "type": "user",
            "attributes": {
              "username": "hendrik"
            }
          }
        },
        "report": {
          "data": {
            "id": "55",
            "type": "report",
            "attributes": {
              "title": "Brute force in login form"
            }
          }
        }
      }
    }
  ]
}

```

Last revised: 2025-05-23

`GET /programs/{id}/triage_reviews`

This endpoint retrieves a list of triage reviews associated with a program. Each triage review includes details such as the rating, comments, and associated report.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Weaknesses

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}/weaknesses" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}/weaknesses',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}/weaknesses',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}/weaknesses");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/weaknesses',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}/weaknesses", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

weaknesses found

```
{
  "data": [
    {
      "id": "1337",
      "type": "weakness",
      "attributes": {
        "name": "Cross-Site Request Forgery (CSRF)",
        "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
        "created_at": "2016-02-02T04:05:06.000Z",
        "external_id": "cwe-352"
      }
    },
    {
      "id": "1338",
      "type": "weakness",
      "attributes": {
        "name": "SQL Injection",
        "description": "The software constructs all or part of an SQL command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended SQL command when it is sent to a downstream component.",
        "created_at": "2016-03-02T04:05:06.000Z",
        "external_id": "cwe-89"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-05-23

`GET /programs/{id}/weaknesses`

The Weakness endpoint enables you to retrieve a list of all weaknesses of the program.

Weaknesses can be fetched by sending a GET request to the weaknesses endpoint. When the request is successful, the API will respond with paginated [weakness objects](https://api.hackerone.com/customer-reference#weakness).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Get Program

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/programs/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/programs/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/programs/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/programs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/programs/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

program found

```
{
  "data": {
    "id": "1337",
    "type": "program",
    "attributes": {
      "handle": "security",
      "severity_calculation_methods": [
        "cvss_4_0",
        "manual"
      ],
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z"
    },
    "relationships": {
      "groups": {
        "data": [
          {
            "id": "2557",
            "type": "group",
            "attributes": {
              "name": "Standard",
              "created_at": "2016-02-02T04:05:06.000Z",
              "permissions": [
                "report_management",
                "reward_management"
              ]
            }
          },
          {
            "id": "2558",
            "type": "group",
            "attributes": {
              "name": "Admin",
              "created_at": "2016-02-02T04:05:06.000Z",
              "permissions": [
                "user_management",
                "program_management"
              ]
            }
          }
        ]
      },
      "members": {
        "data": [
          {
            "id": "1339",
            "type": "member",
            "attributes": {
              "created_at": "2016-02-02T04:05:06.000Z",
              "permissions": [
                "program_management",
                "report_management",
                "reward_management",
                "user_management"
              ]
            },
            "relationships": {
              "user": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    }
                  }
                }
              }
            }
          }
        ]
      },
      "organization": {
        "data": {
          "id": "14",
          "type": "organization",
          "attributes": {
            "handle": "api-example",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`GET /programs/{id}`

A program object can be fetched by sending a GET request to a unique program object. When the request is successful, the API will respond with a [program object](https://api.hackerone.com/customer-reference#program).

The following program relationships are included: [groups](https://api.hackerone.com/customer-reference#group), [members](https://api.hackerone.com/customer-reference#member), [custom field attributes](https://api.hackerone.com/customer-reference#custom-field-attribute) and [policy attachments](https://api.hackerone.com/customer-reference#attachment).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the program. Find the program ID by [fetching your programs](https://api.hackerone.com/customer-resources#programs-get-your-programs) |

## Assets

### Import assets with CSV file

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -d @- <<EOD
null
EOD

```

```
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

data = null

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

data = null

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "null";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "null";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'multipart/form-data');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"null"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

attachment uploaded

```
{
  "data": {
    "id": "4",
    "type": "asset-import",
    "attributes": {
      "state": "processed",
      "source": "ManualImport",
      "errors": [],
      "created_at": "2022-06-21T13:38:04.672Z",
      "updated_at": "2022-06-21T13:38:04.693Z",
      "processed_new_ids": [
        1001,
        1002
      ],
      "processed_existing_ids": [
        501
      ],
      "processed_updated_ids": [],
      "processed_unchanged_ids": [
        501
      ],
      "archived_ids": []
    }
  }
}

```

Last revised: 2025-05-23

`POST /organizations/{organization_id}/asset_imports`

This API endpoint can be used to bulk import assets into the HackerOne platform and to detect duplicates. When the API call is successful, an [asset import object](https://api.hackerone.com/customer-reference#asset-import) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |

### Retrieve an assets import

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_imports/{asset_import_id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

attachment uploaded

```
{
  "data": {
    "id": "2",
    "type": "asset-import",
    "attributes": {
      "state": "processed",
      "source": "AssetScanner",
      "errors": [],
      "created_at": "2022-06-30T14:17:49.640Z",
      "updated_at": "2022-06-30T14:17:50.040Z",
      "processed_new_ids": [
        1001,
        1002,
        1003
      ],
      "processed_existing_ids": [
        501,
        502
      ],
      "processed_updated_ids": [
        501
      ],
      "processed_unchanged_ids": [
        502
      ],
      "archived_ids": []
    }
  }
}

```

Last revised: 2025-05-23

`GET /organizations/{organization_id}/asset_imports/{asset_import_id}`

This API endpoint can be used retrieve importing status via the API, once an asset import is created it is scheduled for execution.

When the API call is successful, an [asset import object](https://api.hackerone.com/customer-reference#asset-import) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| asset_import_id | path | integer | true | The ID of the asset import. |

### Attach screenshot to asset

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -d @- <<EOD
null
EOD

```

```
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

data = null

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

data = null

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "null";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "null";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'multipart/form-data');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"null"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_screenshots", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

attachment uploaded

```
{
  "id": "1337",
  "type": "asset-screenshot",
  "attributes": {
    "expiring_url": "<url>",
    "created_at": "2022-08-04T04:05:06.000Z",
    "file_name": "paprika.png",
    "content_type": "image/png",
    "file_size": 2871
  }
}

```

Last revised: 2025-05-23

`POST /organizations/{organization_id}/asset_screenshots`

NOTE

This endpoint is only available to HackerOne Assets Enterprise subscription.

This API endpoint can be used to attach a screenshot to an existing asset. When the API call is successful, an [asset screenshot object](https://api.hackerone.com/customer-reference#asset-screenshot) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |

### Get All Asset Tag Categories

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

A list of asset tag categories

```
{
  "data": [
    {
      "id": "1",
      "type": "asset-tag-category",
      "attributes": {
        "name": "Environment"
      }
    },
    {
      "id": "2",
      "type": "asset-tag-category",
      "attributes": {
        "name": "Criticality"
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-12-16

`GET /organizations/{organization_id}/asset_tag_categories`

This API endpoint can be used to list all asset tag categories of an organization. When the request is successful, the API will respond with paginated [asset tag category objects](https://api.hackerone.com/customer-reference#asset-tag-category).

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create Asset Tag Category

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset-tag-category",
    "attributes": {
      "name": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset-tag-category",
    "attributes": {
      "name": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset-tag-category",
    "attributes": {
      "name": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset-tag-category\",\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset-tag-category\",\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset-tag-category\",\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tag_categories", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

asset tag category created

```
{
  "id": "123",
  "type": "asset-tag-category",
  "attributes": {
    "name": "test"
  }
}

```

Last revised: 2025-12-16

`POST /organizations/{organization_id}/asset_tag_categories`

This API endpoint can be used to create new asset tag category. When the API call is successful, [asset tag category object](https://api.hackerone.com/customer-reference#asset-tag-category) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| data | body | object | true | The information to create an asset tag category. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | true | The name of the asset tag category |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset-tag-category |

### Get All Asset Tags

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assets found

```
{
  "data": [
    {
      "id": "2",
      "type": "asset-tag",
      "attributes": {
        "name": "test",
        "category_name": "test",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "relationships": {
        "asset_tag_category": {
          "data": {
            "id": "2",
            "type": "asset-tag-category",
            "attributes": {
              "name": "test"
            }
          }
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2025-12-16

`GET /organizations/{organization_id}/asset_tags`

This API endpoint can be used to list all assets tags of an organization. When the request is successful, the API will respond with paginated [asset tag objects](https://api.hackerone.com/customer-reference#asset-tag).

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create Asset Tag

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset-tag",
    "attributes": {
      "category_id": 0,
      "name": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset-tag",
    "attributes": {
      "category_id": 0,
      "name": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset-tag",
    "attributes": {
      "category_id": 0,
      "name": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset-tag\",\n    \"attributes\": {\n      \"category_id\": 0,\n      \"name\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset-tag\",\n    \"attributes\": {\n      \"category_id\": 0,\n      \"name\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset-tag\",\n    \"attributes\": {\n      \"category_id\": 0,\n      \"name\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/asset_tags", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

asset tag created

```
{
  "data": {
    "id": "123",
    "type": "asset-tag",
    "attributes": {
      "name": "Ruby",
      "category_name": "Technology",
      "created_at": "2024-01-15T10:30:00.000Z",
      "updated_at": "2024-01-15T10:30:00.000Z"
    },
    "relationships": {
      "asset_tag_category": {
        "data": {
          "id": "45",
          "type": "asset-tag-category",
          "attributes": {
            "name": "Technology"
          }
        }
      }
    }
  }
}

```

bad request - asset tag already exists

```
{
  "errors": [
    {
      "status": 400,
      "title": "Validation Failed",
      "detail": "Name has already been taken",
      "source": {
        "parameter": "name"
      }
    }
  ]
}

```

not found - organization or category does not exist

```
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "detail": "The requested organization or asset tag category could not be found"
    }
  ]
}

```

Last revised: 2025-12-16

`POST /organizations/{organization_id}/asset_tags`

This API endpoint can be used to create asset tags for an organization. When the request is successful, the API will respond with an [asset tag object](https://api.hackerone.com/customer-reference#asset-tag).

You can get the ID of your organization from me/organizations endpoint. You can get the asset tag category IDs from the get all asset tag categories endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| data | body | object | true | The information to create an asset tag. |
| » type | body | string | true | The type of the resource. Must be "asset-tag". |
| » attributes | body | object | true | none |
| »» category_id | body | integer | true | The ID of the asset tag category this tag belongs to. |
| »» name | body | string | true | The name of the asset tag. Must be unique within the category. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset-tag |

### List asset ports

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "id": "string",
      "type": "asset-port",
      "attributes": {
        "port": 0,
        "protocol": "tcp",
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

Last revised: 2026-04-07

`GET /organizations/{organization_id}/assets/{asset_id}/ports`

This API endpoint returns a list of ports associated with a specific asset. Ports are ordered by port number and protocol (ascending).

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |

### Create asset port

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset-port",
    "attributes": {
      "port": 1,
      "protocol": "tcp"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset-port",
    "attributes": {
      "port": 1,
      "protocol": "tcp"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset-port",
    "attributes": {
      "port": 1,
      "protocol": "tcp"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset-port\",\n    \"attributes\": {\n      \"port\": 1,\n      \"protocol\": \"tcp\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset-port\",\n    \"attributes\": {\n      \"port\": 1,\n      \"protocol\": \"tcp\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset-port\",\n    \"attributes\": {\n      \"port\": 1,\n      \"protocol\": \"tcp\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

201 Response

```
{
  "data": {
    "id": "string",
    "type": "asset-port",
    "attributes": {
      "port": 0,
      "protocol": "tcp",
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-07

`POST /organizations/{organization_id}/assets/{asset_id}/ports`

This API endpoint can be used to add a port to an asset. When the API call is successful, the created port object will be returned.

Each asset can have a maximum of 100 ports. Ports must be between 1 and 65535. Each port/protocol combination must be unique per asset.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| data | body | object | true | The information to create a port. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» port | body | integer | true | Port number (1-65535) |
| »» protocol | body | string | false | Protocol type (tcp or udp). Defaults to tcp if not specified. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset-port |
| »» protocol | tcp |
| »» protocol | udp |

### Delete asset port

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/ports/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

403 Response

```
{
  "errors": [
    {
      "status": 0,
      "title": "string",
      "detail": "string"
    }
  ]
}

```

Last revised: 2026-04-07

`DELETE /organizations/{organization_id}/assets/{asset_id}/ports/{id}`

This API endpoint can be used to delete a port from an asset. When the API call is successful, a 204 No Content response will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| id | path | integer | true | The ID of the port |

### Get Asset Reachability Status

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "asset-reachability",
    "attributes": {
      "last_status": "string",
      "refreshable": true,
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-07

`GET /organizations/{organization_id}/assets/{asset_id}/reachability`

Get the current reachability status for an asset. This endpoint returns the most recent reachability check result, including when the check was last performed and whether a refresh is available.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| asset_id | path | integer | true | The ID of the asset. |

### Check Asset Reachability

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/reachability/check", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "asset-reachability",
    "attributes": {
      "last_status": "string",
      "refreshable": true,
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-07

`POST /organizations/{organization_id}/assets/{asset_id}/reachability/check`

Trigger a reachability check for an asset.

This endpoint performs an active check of the asset's availability. If a check was performed recently (within 1 hour), the cached result will be returned instead.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| asset_id | path | integer | true | The ID of the asset. |

### Get asset scanner configuration

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "asset_scanner_profile",
    "attributes": {
      "enabled": true,
      "last_run_at": "2019-08-24T14:15:22Z",
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-02-06

`GET /organizations/{organization_id}/assets/{asset_id}/scanner`

Retrieve scanner profile configuration for an asset.

Supported Asset Types: - Domain - URL - IP Address

Returns 404 if the asset does not have a scanner profile configured or if the asset type does not support scanning.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |

### Update asset scanner configuration

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner" \
  -X PATCH \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset_scanner_profile",
    "attributes": {
      "enabled": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset_scanner_profile",
    "attributes": {
      "enabled": true
    }
  }
}

r = requests.patch(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset_scanner_profile",
    "attributes": {
      "enabled": true
    }
  }
}

result = RestClient::Request.execute(
  method: :patch,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PATCH");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset_scanner_profile\",\n    \"attributes\": {\n      \"enabled\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset_scanner_profile\",\n    \"attributes\": {\n      \"enabled\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset_scanner_profile\",\n    \"attributes\": {\n      \"enabled\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("PATCH", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scanner", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "asset_scanner_profile",
    "attributes": {
      "enabled": true,
      "last_run_at": "2019-08-24T14:15:22Z",
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-02-06

`PATCH /organizations/{organization_id}/assets/{asset_id}/scanner`

Enable or disable automated scanning for an asset.

Supported Asset Types: - Domain - URL - IP Address

When enabling the scanner for the first time, a scanner profile will be created automatically with a default weekly schedule.

When disabling the scanner, the scanner profile will be updated but not deleted.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| data | body | object | true | none |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» enabled | body | boolean | true | Whether to enable or disable the scanner |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset_scanner_profile |

### Add asset to scope

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_on_changes": true
    },
    "relationships": {
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_on_changes": true
    },
    "relationships": {
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      }
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_on_changes": true
    },
    "relationships": {
      "programs": {
        "data": [
          {
            "id": 0,
            "type": "program"
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_on_changes\": true\n    },\n    \"relationships\": {\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_on_changes\": true\n    },\n    \"relationships\": {\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_on_changes\": true\n    },\n    \"relationships\": {\n      \"programs\": {\n        \"data\": [\n          {\n            \"id\": 0,\n            \"type\": \"program\"\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

structured scopes created

```
{
  "data": [
    {
      "id": "57",
      "type": "structured-scope",
      "attributes": {
        "asset_identifier": "api.example.com",
        "asset_type": "URL",
        "confidentiality_requirement": "high",
        "integrity_requirement": "high",
        "availability_requirement": "high",
        "max_severity": "critical",
        "created_at": "2015-02-02T04:05:06.000Z",
        "updated_at": "2016-05-02T04:05:06.000Z",
        "instruction": "Test with credentials provided in the credential manager",
        "eligible_for_bounty": true,
        "eligible_for_submission": true,
        "reference": "H001001"
      }
    }
  ]
}

```

Last revised: 2025-10-10

`POST /organizations/{organization_id}/assets/{asset_id}/scopes`

This API endpoint can be used to add asset to scope of specified programs. When the API call is successful, [structured scope objects](https://api.hackerone.com/customer-reference#structured-scope) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| data | body | object | true | The information to create a structured scope. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» eligible_for_submission | body | boolean | true | If the asset is eligible for submission. |
| »» eligible_for_bounty | body | boolean | true | If the asset is eligible for bounty. |
| »» instruction | body | string | false | Instructions or additional details about the scope. |
| »» notify_subscribers_on_changes | body | boolean | false | Whether to notify subscribers on this activity. The default is true. |
| » relationships | body | object | true | none |
| »» programs | body | object | true | A list of programs for asset to be added to. |
| »»» data | body | [any] | false | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | structured-scope |

### Update asset scope

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_of_changes": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_of_changes": true
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "structured-scope",
    "attributes": {
      "eligible_for_submission": true,
      "eligible_for_bounty": true,
      "instruction": "string",
      "notify_subscribers_of_changes": true
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_of_changes\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_of_changes\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"structured-scope\",\n    \"attributes\": {\n      \"eligible_for_submission\": true,\n      \"eligible_for_bounty\": true,\n      \"instruction\": \"string\",\n      \"notify_subscribers_of_changes\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

structured scope updated

```
{
  "data": {
    "id": "57",
    "type": "structured-scope",
    "attributes": {
      "asset_identifier": "api.example.com",
      "asset_type": "URL",
      "confidentiality_requirement": "high",
      "integrity_requirement": "high",
      "availability_requirement": "high",
      "max_severity": "critical",
      "created_at": "2015-02-02T04:05:06.000Z",
      "updated_at": "2016-05-02T04:05:06.000Z",
      "instruction": "Test with credentials provided in the credential manager",
      "eligible_for_bounty": true,
      "eligible_for_submission": true,
      "reference": "H001001"
    }
  }
}

```

Last revised: 2025-10-10

`PUT /organizations/{organization_id}/assets/{asset_id}/scopes/{id}`

This API endpoint can be used to update an asset scope for a program. When the API call is successful, a [structured scope object](https://api.hackerone.com/customer-reference#structured-scope) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| id | path | integer | true | The ID of the structured scope |
| data | body | object | true | The information to update a structured scope. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» eligible_for_submission | body | boolean | false | If the asset is eligible for submission. |
| »» eligible_for_bounty | body | boolean | false | If the asset is eligible for bounty. |
| »» instruction | body | string | false | Instructions or additional details about the scope. |
| »» notify_subscribers_of_changes | body | boolean | false | Whether to notify subscribers on this activity. The default is true. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | structured-scope |

### Archive asset scopes

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": [
    {
      "id": 0,
      "type": "program"
    }
  ]
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": [
    {
      "id": 0,
      "type": "program"
    }
  ]
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": [
    {
      "id": 0,
      "type": "program"
    }
  ]
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"program\"\n    }\n  ]\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"program\"\n    }\n  ]\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"program\"\n    }\n  ]\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}/scopes/archive", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

structured scopes archived

```
{
  "data": [
    {
      "id": "57",
      "type": "structured-scope",
      "attributes": {
        "archived_at": "2015-02-02T04:05:06.000Z"
      }
    },
    {
      "id": "58",
      "type": "structured-scope",
      "attributes": {
        "archived_at": "2015-02-02T04:05:06.000Z"
      }
    }
  ]
}

```

Last revised: 2025-10-10

`POST /organizations/{organization_id}/assets/{asset_id}/scopes/archive`

This API endpoint can be used to remove asset from scopes of specified programs. When the API call is successful, [structured scope objects](https://api.hackerone.com/customer-reference#structured-scope) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| data | body | [any] | true | none |

### Get Asset

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

asset found

```
{
  "data": {
    "id": "2",
    "type": "asset",
    "attributes": {
      "asset_type": "domain",
      "identifier": "hackerone.com",
      "domain_name": "hackerone.com",
      "description": null,
      "coverage": "untested",
      "max_severity": "critical",
      "confidentiality_requirement": "high",
      "integrity_requirement": "high",
      "availability_requirement": "high",
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "archived_at": "2017-02-02T04:05:06.000Z",
      "reference": "reference",
      "state": "confirmed"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": "1",
            "type": "asset-tag",
            "attributes": {
              "name": "test"
            },
            "relationships": {
              "asset_tag_category": {
                "data": {
                  "id": "2",
                  "type": "asset-tag-category",
                  "attributes": {
                    "name": "test"
                  }
                }
              }
            }
          }
        ]
      },
      "programs": {
        "data": [
          {
            "id": "1",
            "type": "program",
            "attributes": {
              "handle": "handle",
              "name": "team name"
            }
          }
        ]
      },
      "attachments": {
        "data": [
          {
            "id": "1337",
            "type": "attachment",
            "attributes": {
              "expiring_url": "https://attachments.s3.amazonaws.com/G74PuDP6qdEdN2rpKNLkVwZF",
              "created_at": "2016-02-02T04:05:06.000Z",
              "file_name": "example.png",
              "content_type": "image/png",
              "file_size": 16115
            }
          }
        ]
      },
      "asset_ports": {
        "data": [
          {
            "id": "1",
            "type": "asset-port",
            "attributes": {
              "port": 443,
              "protocol": "tcp",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z"
            }
          },
          {
            "id": "2",
            "type": "asset-port",
            "attributes": {
              "port": 80,
              "protocol": "tcp",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z"
            }
          }
        ]
      },
      "reachability": {
        "data": {
          "id": "1",
          "type": "asset-reachability",
          "attributes": {
            "last_status": "reachable",
            "refreshable": true,
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      }
    }
  }
}

```

Last revised: 2026-01-29

`GET /organizations/{organization_id}/assets/{asset_id}`

An asset object can be fetched by sending a GET request to a unique asset object. In case the request is successful, the API will respond with an [asset object](https://api.hackerone.com/customer-reference#asset).

The following asset relationships are included: [asset tags](https://api.hackerone.com/customer-reference#asset-tag), [programs](https://api.hackerone.com/customer-reference#program), [asset ports](https://api.hackerone.com/customer-reference#asset-port), and [reachability](https://api.hackerone.com/customer-reference#asset-reachability).

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| asset_id | path | integer | true | The ID of the asset. |

### Update Asset

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset",
    "attributes": {
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset",
    "attributes": {
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset",
    "attributes": {
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/{asset_id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assets updated

```
{
  "id": "2",
  "type": "asset",
  "attributes": {
    "asset_type": "domain",
    "domain_name": "hackerone.com",
    "description": null,
    "coverage": "untested",
    "max_severity": "critical",
    "confidentiality_requirement": "high",
    "integrity_requirement": "high",
    "availability_requirement": "high",
    "created_at": "2022-05-19T13:29:47.815Z",
    "updated_at": "2022-05-19T13:29:47.992Z",
    "reference": "reference"
  },
  "relationships": {
    "asset_tags": {
      "data": [
        {
          "id": "1",
          "type": "asset-tag",
          "attributes": {
            "name": "test"
          },
          "relationships": {
            "asset_tag_category": {
              "data": {
                "id": "2",
                "type": "asset-tag-category",
                "attributes": {
                  "name": "test"
                }
              }
            }
          }
        }
      ]
    },
    "programs": {
      "data": [
        {
          "id": "1",
          "type": "program",
          "attributes": {
            "handle": "handle",
            "name": "team name"
          }
        }
      ]
    },
    "attachments": {
      "data": []
    }
  }
}

```

Last revised: 2026-01-29

`PUT /organizations/{organization_id}/assets/{asset_id}`

This API endpoint can be used to update assets in HackerOne platform. When the API call is successful, an [asset object](https://api.hackerone.com/customer-reference#asset) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| asset_id | path | integer | true | The ID of the asset |
| data | body | object | true | The information to update an asset. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» description | body | string | false | The asset description. |
| »» max_severity | body | string | false | The qualitative rating of the maximum severity allowed on this asset. Its value is calculated from the combination of all three of the environmental requirements (CR, IR, and AR). |
| »» confidentiality_requirement | body | string | false | A CVSS environmental modifier that reweights Confidentiality Impact of a vulnerability on this asset. |
| »» integrity_requirement | body | string | false | A CVSS environmental modifier that reweights Integrity Impact of a vulnerability on this asset. |
| »» availability_requirement | body | string | false | A CVSS environmental modifier that reweights Availability Impact of a vulnerability on this asset. |
| »» reference | body | string | false | The customer defined reference identifier or tag of the asset. |
| » relationships | body | object | false | none |
| »» asset_tags | body | object | false | A list of AssetTag objects assigned to the asset. |
| »»» data | body | [any] | false | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset |
| »» max_severity | none |
| »» max_severity | low |
| »» max_severity | medium |
| »» max_severity | high |
| »» max_severity | critical |
| »» confidentiality_requirement | none |
| »» confidentiality_requirement | low |
| »» confidentiality_requirement | high |
| »» integrity_requirement | none |
| »» integrity_requirement | low |
| »» integrity_requirement | high |
| »» availability_requirement | none |
| »» availability_requirement | low |
| »» availability_requirement | high |

### Get All Assets

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/assets", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assets found

```
{
  "data": [
    {
      "id": "2",
      "type": "asset",
      "attributes": {
        "asset_type": "domain",
        "domain_name": "hackerone.com",
        "description": null,
        "coverage": "untested",
        "max_severity": "critical",
        "confidentiality_requirement": "high",
        "integrity_requirement": "high",
        "availability_requirement": "high",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z",
        "archived_at": "2017-02-02T04:05:06.000Z",
        "reference": "reference",
        "state": "confirmed"
      },
      "relationships": {
        "asset_tags": {
          "data": [
            {
              "id": "1",
              "type": "asset-tag",
              "attributes": {
                "name": "test"
              },
              "relationships": {
                "asset_tag_category": {
                  "data": {
                    "id": "2",
                    "type": "asset-tag-category",
                    "attributes": {
                      "name": "test"
                    }
                  }
                }
              }
            }
          ]
        },
        "programs": {
          "data": [
            {
              "id": "1",
              "type": "program",
              "attributes": {
                "handle": "handle",
                "name": "team name"
              }
            }
          ]
        },
        "attachments": {
          "data": [
            {
              "id": "1337",
              "type": "attachment",
              "attributes": {
                "expiring_url": "https://attachments.s3.amazonaws.com/G74PuDP6qdEdN2rpKNLkVwZF",
                "created_at": "2016-02-02T04:05:06.000Z",
                "file_name": "example.png",
                "content_type": "image/png",
                "file_size": 16115
              }
            }
          ]
        }
      }
    }
  ],
  "links": {}
}

```

Last revised: 2026-01-29

`GET /organizations/{organization_id}/assets`

Multiple asset objects can be queried that meet certain filtering criteria by sending a GET request to the assets endpoint. When the request is successful, the API will respond with paginated [asset objects](https://api.hackerone.com/customer-reference#asset).

The following asset relationships are included: [asset tags](https://api.hackerone.com/customer-reference#asset-tag) and [programs](https://api.hackerone.com/customer-reference#program).

You can get the ID of your organization from me/organizations endpoint.

Note, maximum of 10,000 assets can be fetched using the pagination parameters. To fetch more assets, please use the`filter[id__gt]` parameter instead of the pagination parameters. Results are sorted by ID in ascending order.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| filter[asset_tag_ids][] | query | array[int] | false | Filter by the asset's tags IDs you want to fetch the assets for. |
| filter[asset_types][] | query | array[string] | false | Filter by the asset's types you want to fetch the assets for. |
| filter[coverage] | query | array[string] | false | Filter by the asset's coverage you want to fetch the assets for. |
| filter[identifier] | query | string | false | Filter by the asset's identifier you want to fetch the assets for. |
| filter[state][] | query | array[string] | false | Filter by current asset state. |
| filter[archived] | query | boolean | false | Filter by the asset's archived status. By default, all active and archived assets are returned. |
| filter[id__gt] | query | integer | false | Filter by the asset's ID that is greater than the ID specified. Results are sorted by ID in ascending order. |
| filter[created_at__gt] | query | string | false | Filter by assets created after the specified date. Use ISO 8601 format (e.g., 2024-01-01). |
| filter[created_at__lt] | query | string | false | Filter by assets created before the specified date. Use ISO 8601 format (e.g., 2024-12-31). |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| filter[asset_types][] | domain |
| filter[asset_types][] | url |
| filter[asset_types][] | wildcard |
| filter[asset_types][] | androidPlayStore |
| filter[asset_types][] | androidApk |
| filter[asset_types][] | otherAsset |
| filter[asset_types][] | hardware |
| filter[asset_types][] | sourceCode |
| filter[asset_types][] | windowsMicrosoftStore |
| filter[asset_types][] | iosAppStore |
| filter[asset_types][] | iosIpa |
| filter[asset_types][] | iosTestflight |
| filter[asset_types][] | executable |
| filter[asset_types][] | cidr |
| filter[asset_types][] | smartContract |
| filter[asset_types][] | aiModel |
| filter[asset_types][] | api |
| filter[asset_types][] | awsCloudConfig |
| filter[asset_types][] | azureCloudConfig |
| filter[coverage] | all |
| filter[coverage] | new |
| filter[coverage] | in_scope |
| filter[coverage] | out_of_scope |
| filter[coverage] | untested |
| filter[state][] | confirmed |
| filter[state][] | rejected |
| filter[state][] | unconfirmed |

### Create Asset

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "asset",
    "attributes": {
      "asset_type": "domain",
      "identifier": "string",
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "asset",
    "attributes": {
      "asset_type": "domain",
      "identifier": "string",
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "asset",
    "attributes": {
      "asset_type": "domain",
      "identifier": "string",
      "description": "string",
      "max_severity": "none",
      "confidentiality_requirement": "none",
      "integrity_requirement": "none",
      "availability_requirement": "none",
      "reference": "string"
    },
    "relationships": {
      "asset_tags": {
        "data": [
          {
            "id": 0
          }
        ]
      }
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"asset_type\": \"domain\",\n      \"identifier\": \"string\",\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"asset_type\": \"domain\",\n      \"identifier\": \"string\",\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"asset\",\n    \"attributes\": {\n      \"asset_type\": \"domain\",\n      \"identifier\": \"string\",\n      \"description\": \"string\",\n      \"max_severity\": \"none\",\n      \"confidentiality_requirement\": \"none\",\n      \"integrity_requirement\": \"none\",\n      \"availability_requirement\": \"none\",\n      \"reference\": \"string\"\n    },\n    \"relationships\": {\n      \"asset_tags\": {\n        \"data\": [\n          {\n            \"id\": 0\n          }\n        ]\n      }\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assets created

```
{
  "id": "2",
  "type": "asset",
  "attributes": {
    "asset_type": "domain",
    "domain_name": "hackerone.com",
    "description": null,
    "coverage": "untested",
    "max_severity": "critical",
    "confidentiality_requirement": "high",
    "integrity_requirement": "high",
    "availability_requirement": "high",
    "created_at": "2022-05-19T13:29:47.815Z",
    "updated_at": "2022-05-19T13:29:47.992Z",
    "reference": "reference"
  },
  "relationships": {
    "asset_tags": {
      "data": [
        {
          "id": "1",
          "type": "asset-tag",
          "attributes": {
            "name": "test"
          },
          "relationships": {
            "asset_tag_category": {
              "data": {
                "id": "2",
                "type": "asset-tag-category",
                "attributes": {
                  "name": "test"
                }
              }
            }
          }
        }
      ]
    },
    "programs": {
      "data": [
        {
          "id": "1",
          "type": "program",
          "attributes": {
            "handle": "handle",
            "name": "team name"
          }
        }
      ]
    },
    "attachments": {
      "data": []
    }
  }
}

```

Last revised: 2026-01-29

`POST /organizations/{organization_id}/assets`

This API endpoint can be used to create/import assets into the HackerOne platform and to detect duplicates. When the API call is successful, an [asset object](https://api.hackerone.com/customer-reference#asset) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| data | body | object | true | The information to create an asset. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» asset_type | body | string | true | The type of the asset |
| »» identifier | body | string | true | The identifier of the asset. |
| »» description | body | string | false | The asset description. |
| »» max_severity | body | string | false | The qualitative rating of the maximum severity allowed on this asset. Its value is calculated from the combination of all three of the environmental requirements (CR, IR, and AR). |
| »» confidentiality_requirement | body | string | false | A CVSS environmental modifier that reweights Confidentiality Impact of a vulnerability on this asset. |
| »» integrity_requirement | body | string | false | A CVSS environmental modifier that reweights Integrity Impact of a vulnerability on this asset. |
| »» availability_requirement | body | string | false | A CVSS environmental modifier that reweights Availability Impact of a vulnerability on this asset. |
| »» reference | body | string | false | The customer defined reference identifier or tag of the asset. |
| » relationships | body | object | false | none |
| »» asset_tags | body | object | false | A list of AssetTag objects assigned to the asset. |
| »»» data | body | [any] | false | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | asset |
| »» asset_type | domain |
| »» asset_type | url |
| »» asset_type | wildcard |
| »» asset_type | androidPlayStore |
| »» asset_type | androidApk |
| »» asset_type | otherAsset |
| »» asset_type | hardware |
| »» asset_type | sourceCode |
| »» asset_type | windowsMicrosoftStore |
| »» asset_type | iosAppStore |
| »» asset_type | iosIpa |
| »» asset_type | iosTestflight |
| »» asset_type | executable |
| »» asset_type | cidr |
| »» asset_type | smartContract |
| »» asset_type | aiModel |
| »» asset_type | api |
| »» asset_type | awsCloudConfig |
| »» asset_type | azureCloudConfig |
| »» max_severity | none |
| »» max_severity | low |
| »» max_severity | medium |
| »» max_severity | high |
| »» max_severity | critical |
| »» confidentiality_requirement | none |
| »» confidentiality_requirement | low |
| »» confidentiality_requirement | high |
| »» integrity_requirement | none |
| »» integrity_requirement | low |
| »» integrity_requirement | high |
| »» availability_requirement | none |
| »» availability_requirement | low |
| »» availability_requirement | high |

### Archive Assets

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": [
    {
      "id": 0,
      "type": "asset"
    }
  ]
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": [
    {
      "id": 0,
      "type": "asset"
    }
  ]
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": [
    {
      "id": 0,
      "type": "asset"
    }
  ]
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"asset\"\n    }\n  ]\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"asset\"\n    }\n  ]\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": [\n    {\n      \"id\": 0,\n      \"type\": \"asset\"\n    }\n  ]\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/assets/archive", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assets archived

```
{
  "data": [
    {
      "id": "1",
      "type": "asset",
      "attributes": {
        "archived_at": "2015-02-02T04:05:06.000Z"
      }
    },
    {
      "id": "2",
      "type": "asset",
      "attributes": {
        "archived_at": "2015-02-02T04:05:06.000Z"
      }
    }
  ]
}

```

Last revised: 2026-01-29

`POST /organizations/{organization_id}/assets/archive`

This API endpoint can be used to archive assets in HackerOne platform. When the API call is successful, an [asset object](https://api.hackerone.com/customer-reference#asset) will be returned.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| data | body | [any] | true | The information to archive an asset. |

## Automations

### Get All Automations

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/automations", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "type": "automation",
      "id": "string",
      "attributes": {
        "uid": "string",
        "title": "string",
        "enabled": true,
        "archived": true,
        "run_once_per_report": true,
        "events": [
          "string"
        ],
        "template_identifier": "string",
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z"
      }
    }
  ],
  "links": {
    "self": "string",
    "next": "string"
  }
}

```

Last revised: 2026-03-09

`GET /organizations/{organization_id}/automations`

This API endpoint can be used to list all automations for an organization. When the request is successful, the API will respond with paginated automation objects.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

### Create Automation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "template_identifier": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "template_identifier": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "template_identifier": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"template_identifier\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"template_identifier\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"template_identifier\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/automations", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

201 Response

```
{
  "data": {
    "type": "automation",
    "id": "string",
    "attributes": {
      "uid": "string",
      "title": "string",
      "enabled": true,
      "archived": true,
      "run_once_per_report": true,
      "events": [
        "string"
      ],
      "template_identifier": "string",
      "code": "string",
      "config": {},
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-03-09

`POST /organizations/{organization_id}/automations`

This API endpoint can be used to create a new automation for an organization. When the request is successful, the API will respond with the created automation object.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| data | body | object | true | none |
| » type | body | string | true | Must be "automation" |
| » attributes | body | object | true | none |
| »» title | body | string | true | The title of the automation |
| »» code | body | string | true | The executable code of the automation |
| »» template_identifier | body | string | true | The template identifier (e.g. "custom") |
| »» config | body | object | false | The configuration object for the automation |
| »» events | body | [string] | false | The events that trigger this automation |
| »» enabled | body | boolean | false | Whether the automation is enabled |
| »» run_once_per_report | body | boolean | false | Whether the automation should run only once per report |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | automation |

### Get Automation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "type": "automation",
    "id": "string",
    "attributes": {
      "uid": "string",
      "title": "string",
      "enabled": true,
      "archived": true,
      "run_once_per_report": true,
      "events": [
        "string"
      ],
      "template_identifier": "string",
      "code": "string",
      "config": {},
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-03-09

`GET /organizations/{organization_id}/automations/{automation_id}`

This API endpoint can be used to get a specific automation of an organization. When the request is successful, the API will respond with an automation object.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |

### Update Automation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}" \
  -X PATCH \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}

r = requests.patch(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "automation",
    "attributes": {
      "title": "string",
      "code": "string",
      "config": {},
      "events": [
        "string"
      ],
      "enabled": true,
      "run_once_per_report": true
    }
  }
}

result = RestClient::Request.execute(
  method: :patch,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PATCH");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"automation\",\n    \"attributes\": {\n      \"title\": \"string\",\n      \"code\": \"string\",\n      \"config\": {},\n      \"events\": [\n        \"string\"\n      ],\n      \"enabled\": true,\n      \"run_once_per_report\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("PATCH", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "type": "automation",
    "id": "string",
    "attributes": {
      "uid": "string",
      "title": "string",
      "enabled": true,
      "archived": true,
      "run_once_per_report": true,
      "events": [
        "string"
      ],
      "template_identifier": "string",
      "code": "string",
      "config": {},
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-03-09

`PATCH /organizations/{organization_id}/automations/{automation_id}`

This API endpoint can be used to update an existing automation. All fields in the request body are optional — only the provided fields will be updated.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |
| data | body | object | true | none |
| » type | body | string | true | Must be "automation" |
| » attributes | body | object | false | none |
| »» title | body | string | false | The title of the automation |
| »» code | body | string | false | The executable code of the automation |
| »» config | body | object | false | The configuration object for the automation |
| »» events | body | [string] | false | The events that trigger this automation |
| »» enabled | body | boolean | false | Whether the automation is enabled |
| »» run_once_per_report | body | boolean | false | Whether the automation should run only once per report |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | automation |

### Get All Automation Runs

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "type": "automation-run",
      "id": "string",
      "attributes": {
        "status": "running",
        "human_status": "string",
        "comment": "string",
        "created_at": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

Last revised: 2026-03-09

`GET /organizations/{organization_id}/automations/{automation_id}/runs`

This API endpoint can be used to list all runs for a specific automation. When the request is successful, the API will respond with paginated automation run objects.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |
| filter[status] | query | any | false | Filter automation runs by status. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| filter[status] | running |
| filter[status] | success |
| filter[status] | completed_with_errors |
| filter[status] | not_executed |
| filter[status] | failed |
| filter[status] | noop |

### Trigger Automation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "automation-run",
    "attributes": {
      "activity_database_id": 0
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "automation-run",
    "attributes": {
      "activity_database_id": 0
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "automation-run",
    "attributes": {
      "activity_database_id": 0
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"automation-run\",\n    \"attributes\": {\n      \"activity_database_id\": 0\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"automation-run\",\n    \"attributes\": {\n      \"activity_database_id\": 0\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"automation-run\",\n    \"attributes\": {\n      \"activity_database_id\": 0\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

201 Response

```
{
  "data": {
    "type": "automation-run",
    "id": "string",
    "attributes": {
      "status": "running",
      "human_status": "string",
      "comment": "string",
      "created_at": "2019-08-24T14:15:22Z"
    },
    "relationships": {
      "automation": {
        "data": {
          "type": "automation",
          "id": "string"
        }
      }
    }
  }
}

```

Last revised: 2026-03-09

`POST /organizations/{organization_id}/automations/{automation_id}/runs`

This API endpoint can be used to manually trigger an automation run. When the request is successful, the API will respond with the created automation run object.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Note: The automation will be executed asynchronously. The response will contain the created run with status "running". You can poll the run details endpoint to check the execution status.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |
| data | body | object | true | none |
| » type | body | string | true | Must be "automation-run" |
| » attributes | body | object | false | none |
| »» activity_database_id | body | integer | false | Optional: The activity database ID to associate with this run |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | automation-run |

### Get Automation Run

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "type": "automation-run",
    "id": "string",
    "attributes": {
      "status": "running",
      "human_status": "string",
      "comment": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-03-09

`GET /organizations/{organization_id}/automations/{automation_id}/runs/{run_id}`

This API endpoint can be used to get a specific automation run. When the request is successful, the API will respond with an automation run object.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |
| run_id | path | integer | true | The ID of the automation run. |

### Get Automation Run Logs

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "type": "automation-run-logs",
    "id": "string",
    "attributes": {
      "log_messages": [
        {
          "timestamp": "2019-08-24T14:15:22Z",
          "message": "string"
        }
      ]
    }
  }
}

```

Last revised: 2026-03-09

`GET /organizations/{organization_id}/automations/{automation_id}/runs/{run_id}/logs`

This API endpoint can be used to get the logs for a specific automation run. When the request is successful, the API will respond with an array of log messages.

Required permissions: The API token must have Organization Administrator permissions. You can create API tokens in your organization settings. Insufficient permissions will result in a 404 Not Found response.

You can get the ID of your organization from me/organizations endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization. |
| automation_id | path | integer | true | The ID of the automation. |
| run_id | path | integer | true | The ID of the automation run. |

## Findings

### Get All Workboards

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "id": "string",
      "type": "workboard",
      "attributes": {
        "name": "string",
        "position": 0,
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z"
      },
      "relationships": {
        "organization": {
          "data": {
            "type": "organization",
            "id": "string"
          }
        },
        "views": {
          "data": [
            {
              "type": "workboard-view",
              "id": "string"
            }
          ],
          "links": {
            "related": "http://example.com"
          }
        }
      },
      "links": {
        "self": "http://example.com"
      },
      "meta": {
        "views_count": 0
      }
    }
  ],
  "links": {
    "self": "http://example.com",
    "next": "http://example.com"
  },
  "meta": {
    "total_count": 0
  }
}

```

Last revised: 2026-04-23

`GET /organizations/{organization_id}/findings/workboards`

This API endpoint can be used to list all workboards in an organization. Workboards are used to organize and manage vulnerability findings. The endpoint supports cursor-based pagination using the page[size] and page[after] parameters.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page[size] | query | number | false | Number of results to return per page (default: 25, max: 100) |
| page[after] | query | string | false | Cursor for pagination. Use the value from links.next in the previous response. |
| organization_id | path | integer | true | The ID of the organization |

### Create Workboard

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

201 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard",
    "attributes": {
      "name": "string",
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-23

`POST /organizations/{organization_id}/findings/workboards`

Creates a new workboard in the organization. Workboards are used to organize and manage vulnerability findings into different boards.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | true | The name of the workboard |
| organization_id | path | integer | true | The ID of the organization |

### Get Workboard

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard",
    "attributes": {
      "name": "string",
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    },
    "relationships": {
      "organization": {},
      "views": {
        "data": [
          {}
        ],
        "links": {
          "related": "http://example.com"
        }
      }
    },
    "links": {
      "self": "http://example.com",
      "views": "http://example.com"
    },
    "meta": {
      "views_count": 0
    }
  }
}

```

Last revised: 2026-04-23

`GET /organizations/{organization_id}/findings/workboards/{id}`

Retrieves details of a specific workboard including its associated views and metadata.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| id | path | integer | true | The ID of the workboard |

### Update Workboard

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}" \
  -X PATCH \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}

r = requests.patch(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :patch,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PATCH");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PATCH", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard",
    "attributes": {
      "name": "string",
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-23

`PATCH /organizations/{organization_id}/findings/workboards/{id}`

Updates a workboard's properties. Currently supports updating the name field.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | true | The new name for the workboard |
| organization_id | path | integer | true | The ID of the organization |
| id | path | integer | true | The ID of the workboard |

### Delete Workboard

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard",
    "attributes": {
      "name": "string",
      "deleted": true
    }
  }
}

```

Last revised: 2026-04-23

`DELETE /organizations/{organization_id}/findings/workboards/{id}`

Deletes a workboard. This will also delete all views associated with the workboard.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| id | path | integer | true | The ID of the workboard |

### Get All Views

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "id": "string",
      "type": "workboard-view",
      "attributes": {
        "name": "string",
        "query": "string",
        "sort": {
          "field": "string",
          "direction": "asc"
        },
        "columns": [
          "string"
        ],
        "position": 0,
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z"
      },
      "relationships": {
        "workboard": {
          "data": {
            "type": "workboard",
            "id": "string"
          }
        }
      },
      "links": {
        "self": "http://example.com",
        "reports": "http://example.com"
      },
      "meta": {
        "reports_count": 0,
        "query_syntax": "elasticsearch"
      }
    }
  ],
  "links": {
    "self": "http://example.com",
    "next": "http://example.com"
  },
  "meta": {
    "total_count": 0
  }
}

```

Last revised: 2026-04-23

`GET /organizations/{organization_id}/findings/workboards/{workboard_id}/views`

Lists all views within a workboard. Views are filtered perspectives of findings with custom query strings, sort states, and column configurations. The endpoint supports cursor-based pagination.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page[size] | query | number | false | Number of results to return per page (default: 25, max: 100) |
| page[after] | query | string | false | Cursor for pagination. Use the value from links.next in the previous response. |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |

### Create View

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\",\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\",\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"name\": \"string\",\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

201 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard-view",
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {},
      "columns": [
        "string"
      ],
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-23

`POST /organizations/{organization_id}/findings/workboards/{workboard_id}/views`

Creates a new view within a workboard. Views allow you to define custom filters, sort orders, and column configurations for organizing findings.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | none |
| » attributes | body | object | true | none |
| »» name | body | string | true | The name of the view |
| »» query | body | string | false | Elasticsearch query string for filtering findings (optional, defaults to empty string) |
| »» sort | body | object | false | Sort configuration (optional, defaults to id/asc) |
| »»» field | body | string | false | Field to sort by |
| »»» direction | body | string | false | none |
| »» columns | body | [string] | false | Array of column names to display (optional, defaults to id, title, submitted_at) |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |

Enumerated Values

| Parameter | Value |
| --- | --- |
| »»» direction | asc |
| »»» direction | desc |

### Get View

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard-view",
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {},
      "columns": [
        "string"
      ],
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    },
    "relationships": {
      "workboard": {}
    },
    "links": {
      "self": "http://example.com",
      "reports": "http://example.com"
    },
    "meta": {
      "reports_count": 0,
      "query_syntax": "elasticsearch"
    }
  }
}

```

Last revised: 2026-04-23

`GET /organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}`

Retrieves details of a specific view including its query configuration, sort state, columns, and associated metadata.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |
| id | path | integer | true | The ID of the view |

### Update View

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}" \
  -X PATCH \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}

r = requests.patch(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "query": "string",
      "sort": {
        "field": "string",
        "direction": "asc"
      },
      "columns": [
        "string"
      ]
    }
  }
}

result = RestClient::Request.execute(
  method: :patch,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PATCH");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"query\": \"string\",\n      \"sort\": {\n        \"field\": \"string\",\n        \"direction\": \"asc\"\n      },\n      \"columns\": [\n        \"string\"\n      ]\n    }\n  }\n}"`))

    req, err := http.NewRequest("PATCH", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard-view",
    "attributes": {
      "name": "string",
      "query": "string",
      "sort": {},
      "columns": [
        "string"
      ],
      "position": 0,
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  }
}

```

Last revised: 2026-04-23

`PATCH /organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}`

Updates a view's properties including query string, sort configuration, and visible columns. All fields are optional in the update request.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | none |
| » attributes | body | object | true | none |
| »» query | body | string | false | Elasticsearch query string for filtering findings |
| »» sort | body | object | false | Sort configuration |
| »»» field | body | string | false | none |
| »»» direction | body | string | false | none |
| »» columns | body | [string] | false | Array of column names to display |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |
| id | path | integer | true | The ID of the view |

Enumerated Values

| Parameter | Value |
| --- | --- |
| »»» direction | asc |
| »»» direction | desc |

### Delete View

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": {
    "id": "string",
    "type": "workboard-view",
    "attributes": {
      "name": "string",
      "deleted": true
    }
  }
}

```

Last revised: 2026-04-23

`DELETE /organizations/{organization_id}/findings/workboards/{workboard_id}/views/{id}`

Deletes a view from the workboard. This removes the saved filter configuration but does not affect any findings.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |
| id | path | integer | true | The ID of the view |

### Get View Reports

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

200 Response

```
{
  "data": [
    {
      "id": "string",
      "type": "report",
      "attributes": {
        "database_id": "string",
        "graphql_id": "string",
        "reference": "string",
        "reference_url": "string",
        "title": "string",
        "state": "string",
        "substate": "string",
        "severity": "string",
        "vulnerability_information": "string",
        "submitted_at": "2019-08-24T14:15:22Z",
        "triaged_at": "2019-08-24T14:15:22Z",
        "closed_at": "2019-08-24T14:15:22Z",
        "disclosed_at": "2019-08-24T14:15:22Z",
        "last_activity_at": "2019-08-24T14:15:22Z",
        "activities_count": 0,
        "tags": [
          "string"
        ],
        "ineligible_for_bounty": true,
        "bounties_total_awarded_amount": 0,
        "bounties": {},
        "reporter": {},
        "weakness": {},
        "assigned_to_user": {},
        "assigned_to_group": {},
        "structured_scope": {},
        "engagement": {},
        "inboxes": [],
        "campaign": {},
        "response_targets": {},
        "spot_check": {},
        "mediation_request": {},
        "last_comment_by_reporter": {},
        "participants": {}
      }
    }
  ],
  "links": {
    "self": "http://example.com"
  },
  "meta": {
    "total_count": 0,
    "page_size": 0
  }
}

```

Last revised: 2026-04-23

`GET /organizations/{organization_id}/findings/workboards/{workboard_id}/views/{view_id}/reports`

Retrieves all findings (reports) that match a view's query configuration. This endpoint executes the view's Elasticsearch query and returns paginated results with the view's sort order applied. Use this to see the actual findings filtered by a specific view.

Required permissions: Organization membership

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page[size] | query | number | false | Number of results to return per page (default: 25, max: 100) |
| page[number] | query | number | false | Page number to retrieve (default: 1) |
| organization_id | path | integer | true | The ID of the organization |
| workboard_id | path | integer | true | The ID of the workboard |
| view_id | path | integer | true | The ID of the view |

## Reports

### Create Comment

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/activities" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "activity-comment",
    "attributes": {
      "message": "string",
      "internal": true,
      "attachment_ids": []
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "activity-comment",
    "attributes": {
      "message": "string",
      "internal": true,
      "attachment_ids": []
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/activities',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "activity-comment",
    "attributes": {
      "message": "string",
      "internal": true,
      "attachment_ids": []
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/activities',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/activities");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"activity-comment\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"internal\": true,\n      \"attachment_ids\": []\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"activity-comment\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"internal\": true,\n      \"attachment_ids\": []\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/activities',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"activity-comment\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"internal\": true,\n      \"attachment_ids\": []\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/activities", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

comment created

```
{
  "data": {
    "id": "1337",
    "type": "activity-comment",
    "attributes": {
      "message": "A fix has been deployed. Can you retest, please?",
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "internal": false
    },
    "relationships": {
      "actor": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/activities`

Both public and internal comments can be posted with this endpoint. Comments require a message before they will be posted. If a public comment is posted, any user that is subscribed to the report will receive a notification of the created comment. For internal comments, only people that are managing the program who are subscribed to the report will receive a notification.

Required permissions: Report Management. Enables you to post public comments. Posting internal comments do not require any additional permissions. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to create a comment object for the report. |
| » type | body | string | true | Type of activity. |
| » attributes | body | object | true | none |
| »» message | body | string | true | The message that will be posted. |
| »» internal | body | boolean | true | A boolean that indicates whether the comment should |
| »» attachment_ids | body | array | false | Array of attachment IDs. You can upload attachments [here](https://api.hackerone.com/customer-resources/#reports-upload-attachments) |

Detailed descriptions

»» internal: A boolean that indicates whether the comment should be internal or public. Internal comments are only viewable by the users that manage the program. Public comments are viewable by everyone, including the person that submitted the report.

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | activity-comment |

### Update Assignee

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/assignee" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "id": 0,
    "type": "user",
    "attributes": {
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "id": 0,
    "type": "user",
    "attributes": {
      "message": "string"
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/assignee',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "id": 0,
    "type": "user",
    "attributes": {
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/assignee',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/assignee");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"id\": 0,\n    \"type\": \"user\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"id\": 0,\n    \"type\": \"user\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/assignee',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"id\": 0,\n    \"type\": \"user\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/assignee", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assignee updated

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": []
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "assignee": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "member",
          "name": "Member",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "activities": {
      "data": [
        {
          "id": "1337",
          "type": "activity-user-assigned-to-bug",
          "attributes": {
            "message": "@member Please check this out!",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z",
            "internal": true
          },
          "relationships": {
            "actor": {
              "data": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api_example_company",
                  "name": null,
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            },
            "assigned_user": {
              "data": {
                "id": "1337",
                "type": "user",
                "attributes": {
                  "username": "member",
                  "name": "Member",
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            }
          }
        }
      ]
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/assignee`

A user or group can be assigned to a report with this endpoint. An optional message can be specified, which will be posted as an internal comment to the report subscribers. Only users and groups that are part of the program can be assigned. It is not possible to assign API users to a report.

When assigning a single user to a report, that user will automatically be subscribed to the report. In case a group is assigned to a report, all users that are part of that group are subscribed to the report. Subscribers will receive a notification that the report was assigned.

In case the request was successful, the API will respond with the updated report object.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | Contains the information to assign a user or group object to the report, or to clear the assignee of a report. |
| » id | body | integer | false | The ID of the user or group. This is required unless the type is 'nobody' |
| » type | body | string | true | Specifies whether a user or group should be assigned, or if the assignee should be cleared. |
| » attributes | body | object | false | none |
| »» message | body | string | false | The message that will be posted to the assigned user or group. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | user |
| » type | group |
| » type | nobody |

### Upload Attachments

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/attachments" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -d @- <<EOD
null
EOD

```

```
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

data = null

r = requests.post(
  'https://api.hackerone.com/v1/reports/attachments',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

data = null

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/attachments',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/attachments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "null";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "null";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'multipart/form-data');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/attachments',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"null"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/attachments", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

attachment uploaded

```
{
  "id": "1337",
  "type": "attachment",
  "attributes": {
    "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
    "created_at": "2016-02-02T04:05:06.000Z",
    "file_name": "root.rb",
    "content_type": "text/x-ruby",
    "file_size": 2871
  }
}

```

Last revised: 2025-10-23

`POST /reports/attachments`

Attachments can be uploaded by sending a POST request to the reports attachments endpoint. When the API call is successful, an [attachment](https://api.hackerone.com/customer-reference#attachment) object will be returned.

You can use the attachment ID to display the attachment in your comments. For example, if the attachment ID is`1337`, then include`{F1337}` in your comments to display the attachment.

File Validation Requirements: - Maximum file size: 250 MB - Maximum filename length: 255 characters - GIF images: Maximum dimensions 1920x1080 pixels

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

### Delete Attachments

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{report_id}/attachments" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>"

```

```
import requests

r = requests.delete(
  'https://api.hackerone.com/v1/reports/{report_id}/attachments',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>')
)

print(r.json())

```

```
require 'rest-client'
require 'json'

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/reports/{report_id}/attachments',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>'
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{report_id}/attachments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));

fetch('https://api.hackerone.com/v1/reports/{report_id}/attachments',
{
  method: 'DELETE'

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/reports/{report_id}/attachments", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Last revised: 2025-10-23

`DELETE /reports/{report_id}/attachments`

All attachments for a report can be permanently deleted by sending a DELETE request to the`/reports/{report_id}/attachments` endpoint. This will remove all attachments associated with the specified report. This action is irreversible.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| report_id | path | string | true | ID of the report. |

### Award Bounty

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/bounties" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/bounties',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/bounties',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/bounties");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/bounties',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/bounties", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

bounty awarded

```
{
  "id": "1337",
  "type": "bounty",
  "attributes": {
    "amount": "500.00",
    "bonus_amount": "50.00",
    "created_at": "2016-02-02T04:05:06.000Z"
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/bounties`

You can use this endpoint to award bounties to the reporter of the provided report.

Required permissions: Reward Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

In addition, your program needs to be able to award bounties and the report needs to be eligible for bounties. If either case is false, the call will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information required to create a bounty. |
| » message | body | string | true | The public message posted on the report. This is always required. |
| » amount | body | number | false | The bounty award to award to the reporter. Only amount or bonus amount is required. It must be a positive number and, when provided, must be equal to or greater than your minimum bounty. |
| » bonus_amount | body | number | false | The bonus amount to award to the reporter. Only amount or bonus amount is required. It must be a positive number. |

### Mark as Ineligible for Bounty

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-ineligible-for-bounty"
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-ineligible-for-bounty"
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-ineligible-for-bounty"
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-ineligible-for-bounty\"\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-ineligible-for-bounty\"\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-ineligible-for-bounty\"\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/ineligible_for_bounty", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Marked as ineligible for bounty

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-01-09

`PUT /reports/{id}/ineligible_for_bounty`

Marking a report as ineligible for bounty through the HackerOne API can be useful to programmatically batch update received reports in HackerOne.

Marking a report as ineligible for bounty can be done through this endpoint. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Reward Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to mark a report as ineligible for bounty. |
| » type | body | string | true | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-ineligible-for-bounty |

### List bounty suggestions

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/bounty_suggestions" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/bounty_suggestions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/reports/{id}/bounty_suggestions", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

bounty suggestions

```
{
  "id": "1337",
  "type": "bounty",
  "attributes": {
    "amount": "500.00",
    "bonus_amount": "50.00",
    "created_at": "2016-02-02T04:05:06.000Z"
  }
}

```

Last revised: 2025-05-23

`GET /reports/{id}/bounty_suggestions`

This API endpoint allows a user to retrieve a list of bounty suggestions for a report.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |

### Create bounty suggestion

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/bounty_suggestions" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "message": "string",
    "amount": 0,
    "bonus_amount": 0
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/bounty_suggestions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/bounty_suggestions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"message\": \"string\",\n    \"amount\": 0,\n    \"bonus_amount\": 0\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/bounty_suggestions", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

bounty suggestion created

```
{
  "id": "1337",
  "type": "activity-bounty-suggested",
  "attributes": {
    "message": "Bounty Suggested!",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "internal": true,
    "bounty_amount": "500",
    "bonus_amount": "50"
  },
  "relationships": {
    "actor": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/bounty_suggestions`

You can use this endpoint to suggest bounties to the provided report.

Required permissions: Reward Management or Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | none |
| » message | body | string | true | (Always required) The internal message posted on the report. Only viewable by team members. |
| » amount | body | integer | false | The suggested bounty award to award the reporter. Only amount or bonus amount is required. It must be a positive number, and, when provided, must be equal to or greater than your minimum amount. |
| » bonus_amount | body | integer | false | The suggested bonus amount to award to the reporter. Only amount or bonus amount is required. It must be a positive number. |

### Close Comments

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/close_comments" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "activity-comments-closed"
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "activity-comments-closed"
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/close_comments',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "activity-comments-closed"
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/close_comments',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/close_comments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"activity-comments-closed\"\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"activity-comments-closed\"\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/close_comments',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"activity-comments-closed\"\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/close_comments", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

comments closed

```
{
  "id": "1337",
  "type": "activity-comments-closed",
  "attributes": {
    "message": "Comments Closed!",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "internal": false
  },
  "relationships": {
    "actor": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/close_comments`

You can use this endpoint to lock the report and the report can only be locked once. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform or reported to other teams.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to lock the report. |
| » type | body | string | true | none |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | activity-comments-closed |

### Manage Custom Field Values

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/custom_field_values" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "custom_field_attribute_id": 0,
      "value": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "custom_field_attribute_id": 0,
      "value": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/custom_field_values',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "custom_field_attribute_id": 0,
      "value": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/custom_field_values',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/custom_field_values");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"custom_field_attribute_id\": 0,\n      \"value\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"custom_field_attribute_id\": 0,\n      \"value\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/custom_field_values',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"custom_field_attribute_id\": 0,\n      \"value\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/custom_field_values", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Custom field updated

```
{
  "id": "1337",
  "type": "custom-field-value",
  "attributes": {
    "value": "Infrastructure",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "custom_field_attribute": {
      "data": {
        "id": "287",
        "type": "custom-field-attribute",
        "attributes": {
          "field_type": "List",
          "label": "Product Squad",
          "internal": false,
          "required": false,
          "error_message": null,
          "helper_text": "Helping you out with this!",
          "configuration": "Infrastructure, Frontend, Backend",
          "checkbox_text": null,
          "regex": null,
          "created_at": "2013-01-01T00:00:00.000Z",
          "updated_at": "2013-01-01T00:00:00.000Z",
          "archived_at": null
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/custom_field_values`

You can use this endpoint to create / update the Custom Field Values of the provided report. If the report already has a value for the provided Custom Field Attribute ID, the value will be replaced. To get a list of existing Custom Field Attributes, see program. This feature is only available to select programs at this time.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information required to create a Custom Field Value. |
| » attributes | body | object | true | none |
| »» custom_field_attribute_id | body | integer | true | The Custom Field Attribute ID for which a value needs to be set. A complete list of available Custom Field Attribute IDs is exposed on the Program object. |
| »» value | body | string | false | The value that needs to be set for the given Custom Field Attribute. Leave this field empty to remove a Custom Field Attribute from a report. |

### Update CVEs

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/cves" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-cves",
    "attributes": {
      "cve_ids": [
        "string"
      ]
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-cves",
    "attributes": {
      "cve_ids": [
        "string"
      ]
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/cves',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-cves",
    "attributes": {
      "cve_ids": [
        "string"
      ]
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/cves',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/cves");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-cves\",\n    \"attributes\": {\n      \"cve_ids\": [\n        \"string\"\n      ]\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-cves\",\n    \"attributes\": {\n      \"cve_ids\": [\n        \"string\"\n      ]\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/cves',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-cves\",\n    \"attributes\": {\n      \"cve_ids\": [\n        \"string\"\n      ]\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/cves", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

CVE IDs updated

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "main_state": "open",
    "state": "new",
    "created_at": "2024-01-20T14:26:19.286Z",
    "submitted_at": "2024-01-20T14:26:19.286Z",
    "vulnerability_information": "Vuln information",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "reporter_agreed_on_going_public_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "cve_ids": [
      "CVE-2024-21075"
    ],
    "source": null,
    "timer_bounty_awarded_elapsed_time": null,
    "timer_bounty_awarded_miss_at": null,
    "timer_first_program_response_miss_at": null,
    "timer_first_program_response_elapsed_time": null,
    "timer_report_resolved_miss_at": null,
    "timer_report_resolved_elapsed_time": null,
    "timer_report_triage_miss_at": null,
    "timer_report_triage_elapsed_time": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "bio": null,
          "website": null,
          "location": null,
          "hackerone_triager": false
        }
      }
    },
    "collaborators": {
      "data": []
    },
    "assignee": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "member",
          "name": "Member",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "signal": null,
          "impact": null,
          "reputation": null,
          "bio": null,
          "website": null,
          "location": null,
          "hackerone_triager": false
        }
      }
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "activities": {
      "data": [
        {
          "type": "activity-cve-id-added",
          "id": "445",
          "attributes": {
            "message": "",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z",
            "internal": false
          },
          "relationships": {
            "actor": {
              "data": {
                "id": "1337",
                "type": "user",
                "attributes": {
                  "username": "member",
                  "name": "Member",
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  },
                  "signal": null,
                  "impact": null,
                  "reputation": null,
                  "bio": null,
                  "website": null,
                  "location": null,
                  "hackerone_triager": false
                }
              }
            }
          }
        }
      ]
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    },
    "inboxes": {
      "data": []
    },
    "custom_field_values": {
      "data": []
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/cves`

Changing the CVE ids of a report can be done through this endpoint. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the CVEs of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» cve_ids | body | [string] | true | The ID's of the CVEs the report should have. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-cves |

### Update Disclosure Request

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/disclosure_requests" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "substate": "full",
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "substate": "full",
      "message": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "substate": "full",
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/disclosure_requests");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"substate\": \"full\",\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"substate\": \"full\",\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"substate\": \"full\",\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/disclosure_requests", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

disclosure_request updated

```
{
  "id": "1337",
  "type": "activity-agreed-on-going-public",
  "attributes": {
    "message": "Agreed On Going Public!",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "internal": false
  },
  "relationships": {
    "actor": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/disclosure_requests`

The program can request disclosure for any closed report.

You can use this endpoint to create the disclosure request for the report which will result in:

The agreement to disclose the report if the reporter has already requested the disclosure. The contents of the report will be made public instantly. The time when the report was disclosed will be returned in the 'disclosed_at' attribute.

The disclosure request if the reporter hasn't requested the disclosure yet. If the reporter doesn't either approve or deny disclosure request from the program, the contents of the report will be auto-disclosed within 30 days. The 'allow_singular_disclosure_at' attribute value will show when the report will be disclosed.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | This object contains the information about disclosure request. |
| » attributes | body | object | true | none |
| »» substate | body | string | true | Select whether you want to disclose the full report ("full") or a |
| »» message | body | string | false | Additional information |

Detailed descriptions

»» substate: Select whether you want to disclose the full report ("full") or a limited version ("no-content"). Possible values: full, no-content

Enumerated Values

| Parameter | Value |
| --- | --- |
| »» substate | full |
| »» substate | no-content |

### Cancel Disclosure Request

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/disclosure_requests" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "message": "string"
    }
  }
}

r = requests.delete(
  'https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/disclosure_requests");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/disclosure_requests',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/reports/{id}/disclosure_requests", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

disclosure request cancelled

```
{
  "id": "1337",
  "type": "activity-cancelled-disclosure-request",
  "attributes": {
    "message": "Cancel disclosure 1",
    "created_at": "2019-10-23T13:35:35.616Z",
    "updated_at": "2019-10-23T13:35:35.616Z",
    "internal": false
  },
  "relationships": {
    "actor": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api_user",
          "name": null,
          "disabled": false,
          "created_at": "2019-10-14T13:59:49.563Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "signal": null,
          "impact": null,
          "reputation": null,
          "bio": null,
          "website": null,
          "location": null,
          "hackerone_triager": false
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`DELETE /reports/{id}/disclosure_requests`

The program can cancel the disclosure request for the provided report.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | none |
| » attributes | body | object | false | none |
| »» message | body | string | false | The message that will be posted. |

### Update inboxes

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/inboxes" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "organization_inbox_ids": []
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "organization_inbox_ids": []
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/inboxes',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "organization_inbox_ids": []
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/inboxes',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/inboxes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"organization_inbox_ids\": []\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"organization_inbox_ids\": []\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/inboxes',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"organization_inbox_ids\": []\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/inboxes", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report updated

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2025-11-10

`POST /reports/{id}/inboxes`

You can use this endpoint to update the inboxes of the provided report. This replaces the custom inboxes of the report.

Note: Reports can only be added and removed from Custom inboxes.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information required to update the report's inboxes. |
| » organization_inbox_ids | body | array | true | The ID's of the inboxes the report should be in. |

### Add participant

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/participants" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-participant",
    "attributes": {
      "email": "string",
      "username": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-participant",
    "attributes": {
      "email": "string",
      "username": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/participants',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-participant",
    "attributes": {
      "email": "string",
      "username": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/participants',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/participants");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-participant\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"username\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-participant\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"username\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/participants',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-participant\",\n    \"attributes\": {\n      \"email\": \"string\",\n      \"username\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/participants", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

invitation sent

```
{
  "id": "117",
  "type": "report-participant",
  "attributes": {
    "report_id": "1337",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/participants`

Participants can be added through this endpoint by an email address or a HackerOne username. It can be useful to programmatically batch update received reports in HackerOne. This API endpoint cannot be used for reports that are published and have been reported outside of the HackerOne platform.

Required permission: Report Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to add a participant. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» email | body | string | false | The email address of the participant. Required when username is not provided. |
| »» username | body | string | false | The HackerOne username of the participant. Required when email address is not provided. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-participant |

### Generate PDF

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/pdf" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>"

```

```
import requests

r = requests.get(
  'https://api.hackerone.com/v1/reports/{id}/pdf',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>')
)

print(r.json())

```

```
require 'rest-client'
require 'json'

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/reports/{id}/pdf',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>'
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/pdf");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));

fetch('https://api.hackerone.com/v1/reports/{id}/pdf',
{
  method: 'GET'

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/reports/{id}/pdf", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Last revised: 2025-03-14

`GET /reports/{id}/pdf`

You can use this endpoint to generate a PDF of a report.

Required permissions: Read only permission for the report. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| pdf_type | query | string | false | The type of PDF to generate. Possible values are: "reporter", "full" or "triage". The default value is "reporter". |

### Redact report

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/redact" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-redact",
    "attributes": {
      "string_to_redact": "string",
      "include_internal": false
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-redact",
    "attributes": {
      "string_to_redact": "string",
      "include_internal": false
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/redact',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-redact",
    "attributes": {
      "string_to_redact": "string",
      "include_internal": false
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/redact',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/redact");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-redact\",\n    \"attributes\": {\n      \"string_to_redact\": \"string\",\n      \"include_internal\": false\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-redact\",\n    \"attributes\": {\n      \"string_to_redact\": \"string\",\n      \"include_internal\": false\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/redact',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-redact\",\n    \"attributes\": {\n      \"string_to_redact\": \"string\",\n      \"include_internal\": false\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/redact", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report redacted

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-02-16

`PUT /reports/{id}/redact`

Reports can be redacted through this endpoint. It can be useful to programmatically batch update received reports in HackerOne. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to redact a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» string_to_redact | body | string | true | The content to be redacted from the report. |
| »» include_internal | body | boolean | false | When set to true, internal comments will also be redacted. Defaults to false. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-redact |

### Escalate Report

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/escalate" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "attributes": {
      "integration_id": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "attributes": {
      "integration_id": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/escalate',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "attributes": {
      "integration_id": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/escalate',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/escalate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"attributes\": {\n      \"integration_id\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"attributes\": {\n      \"integration_id\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/escalate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"attributes\": {\n      \"integration_id\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/escalate", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report escalated

```
{
  "data": {
    "id": "1337",
    "type": "report",
    "attributes": {
      "title": "XSS in login form",
      "state": "new",
      "created_at": "2016-02-02T04:05:06.000Z",
      "vulnerability_information": "...",
      "triaged_at": null,
      "closed_at": null,
      "last_reporter_activity_at": null,
      "first_program_activity_at": null,
      "last_program_activity_at": null,
      "bounty_awarded_at": null,
      "swag_awarded_at": null,
      "disclosed_at": null,
      "source": null
    },
    "relationships": {
      "reporter": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "collaborators": {
        "data": [
          {
            "weight": 1,
            "user": {
              "id": "1337",
              "type": "user",
              "attributes": {
                "username": "api-example",
                "name": "API Example",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          },
          {
            "weight": 1,
            "user": {
              "id": "1338",
              "type": "user",
              "attributes": {
                "username": "api-example 2",
                "name": "API Example 2",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          }
        ]
      },
      "assignee": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "member",
            "name": "Member",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "program": {
        "data": {
          "id": "1337",
          "type": "program",
          "attributes": {
            "handle": "security",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "severity": {
        "data": {
          "id": "57",
          "type": "severity",
          "attributes": {
            "rating": "high",
            "author_type": "User",
            "user_id": 1337,
            "created_at": "2016-02-02T04:05:06.000Z",
            "score": 8.7,
            "attack_complexity": "low",
            "attack_vector": "adjacent",
            "availability": "high",
            "confidentiality": "low",
            "integrity": "high",
            "privileges_required": "low",
            "user_interaction": "required",
            "scope": "changed"
          }
        }
      },
      "swag": {
        "data": []
      },
      "attachments": {
        "data": []
      },
      "weakness": {
        "data": {
          "id": "1337",
          "type": "weakness",
          "attributes": {
            "name": "Cross-Site Request Forgery (CSRF)",
            "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
            "external_id": "cwe-352",
            "created_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "structured_scope": {
        "data": {
          "id": "57",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "url",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2015-02-02T04:05:06.000Z",
            "updated_at": "2016-05-02T04:05:06.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      },
      "campaign": null,
      "activities": {
        "data": [
          {
            "type": "activity-comment",
            "id": "445",
            "attributes": {
              "message": "Comment!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    },
                    "signal": null,
                    "impact": null,
                    "reputation": null,
                    "bio": null,
                    "website": null,
                    "location": null,
                    "hackerone_triager": false
                  }
                }
              },
              "attachments": {
                "data": [
                  {
                    "id": "1337",
                    "type": "attachment",
                    "attributes": {
                      "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
                      "created_at": "2016-02-02T04:05:06.000Z",
                      "file_name": "root.rb",
                      "content_type": "text/x-ruby",
                      "file_size": 2871
                    }
                  }
                ]
              }
            }
          },
          {
            "id": "1337",
            "type": "activity-bug-resolved",
            "attributes": {
              "message": "Bug Resolved!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    }
                  }
                }
              }
            }
          }
        ]
      },
      "bounties": {
        "data": []
      },
      "summaries": {
        "data": []
      },
      "inboxes": {
        "data": [
          {
            "id": "13",
            "type": "inbox",
            "attributes": {
              "name": "HackerOne",
              "type": "default"
            }
          },
          {
            "id": "65",
            "type": "inbox",
            "attributes": {
              "name": "Custom Inbox number one",
              "type": "custom"
            }
          }
        ]
      },
      "triggered_pre_submission_trigger": {
        "data": {
          "id": "1337",
          "type": "trigger",
          "attributes": {
            "title": "Example Trigger"
          }
        }
      },
      "custom_field_values": {
        "data": []
      },
      "automated_remediation_guidance": {
        "data": {
          "id": "1",
          "type": "automated-remediation-guidance",
          "attributes": {
            "reference": "https://cwe.mitre.org/data/definitions/120.html",
            "created_at": "2020-10-23T12:09:37.859Z"
          }
        }
      },
      "custom_remediation_guidance": {
        "data": {
          "id": "84",
          "type": "custom-remediation-guidance",
          "attributes": {
            "message": "Check buffer boundaries if accessing the buffer in a loop and make sure you are not in danger of writing past the allocated space.",
            "created_at": "2020-10-26T08:47:23.296Z"
          },
          "relationships": {
            "author": {
              "data": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api-example-2",
                  "name": "API Example 2",
                  "disabled": false,
                  "created_at": "2020-10-22T011:22:05.402Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Last revised: 2025-12-16

`POST /reports/{id}/escalate`

You can use this endpoint to send a report to the selected issue tracker. The integration_id can be found through the [get program integrations endpoint](https://api.hackerone.com/customer-resources/#programs-get-integrations).

Required permission: Report Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information for escalating report. |
| » attributes | body | object | true | none |
| »» integration_id | body | string | true | The ID of the integration instance. Required for escalating the report. |

### Remove Escalation

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{report_id}/escalate" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete(
  'https://api.hackerone.com/v1/reports/{report_id}/escalate',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/reports/{report_id}/escalate',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{report_id}/escalate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{report_id}/escalate',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/reports/{report_id}/escalate", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

escalation successfully removed from report

```
{
  "data": {
    "id": "1337",
    "type": "report",
    "attributes": {
      "title": "XSS in login form",
      "state": "new",
      "created_at": "2016-02-02T04:05:06.000Z",
      "vulnerability_information": "...",
      "triaged_at": null,
      "closed_at": null,
      "last_reporter_activity_at": null,
      "first_program_activity_at": null,
      "last_program_activity_at": null,
      "bounty_awarded_at": null,
      "swag_awarded_at": null,
      "disclosed_at": null,
      "source": null
    },
    "relationships": {
      "reporter": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "collaborators": {
        "data": [
          {
            "weight": 1,
            "user": {
              "id": "1337",
              "type": "user",
              "attributes": {
                "username": "api-example",
                "name": "API Example",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          },
          {
            "weight": 1,
            "user": {
              "id": "1338",
              "type": "user",
              "attributes": {
                "username": "api-example 2",
                "name": "API Example 2",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          }
        ]
      },
      "assignee": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "member",
            "name": "Member",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "program": {
        "data": {
          "id": "1337",
          "type": "program",
          "attributes": {
            "handle": "security",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "severity": {
        "data": {
          "id": "57",
          "type": "severity",
          "attributes": {
            "rating": "high",
            "author_type": "User",
            "user_id": 1337,
            "created_at": "2016-02-02T04:05:06.000Z",
            "score": 8.7,
            "attack_complexity": "low",
            "attack_vector": "adjacent",
            "availability": "high",
            "confidentiality": "low",
            "integrity": "high",
            "privileges_required": "low",
            "user_interaction": "required",
            "scope": "changed"
          }
        }
      },
      "swag": {
        "data": []
      },
      "attachments": {
        "data": []
      },
      "weakness": {
        "data": {
          "id": "1337",
          "type": "weakness",
          "attributes": {
            "name": "Cross-Site Request Forgery (CSRF)",
            "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
            "external_id": "cwe-352",
            "created_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "structured_scope": {
        "data": {
          "id": "57",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "url",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2015-02-02T04:05:06.000Z",
            "updated_at": "2016-05-02T04:05:06.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      },
      "campaign": null,
      "activities": {
        "data": [
          {
            "type": "activity-comment",
            "id": "445",
            "attributes": {
              "message": "Comment!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    },
                    "signal": null,
                    "impact": null,
                    "reputation": null,
                    "bio": null,
                    "website": null,
                    "location": null,
                    "hackerone_triager": false
                  }
                }
              },
              "attachments": {
                "data": [
                  {
                    "id": "1337",
                    "type": "attachment",
                    "attributes": {
                      "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
                      "created_at": "2016-02-02T04:05:06.000Z",
                      "file_name": "root.rb",
                      "content_type": "text/x-ruby",
                      "file_size": 2871
                    }
                  }
                ]
              }
            }
          },
          {
            "id": "1337",
            "type": "activity-bug-resolved",
            "attributes": {
              "message": "Bug Resolved!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    }
                  }
                }
              }
            }
          }
        ]
      },
      "bounties": {
        "data": []
      },
      "summaries": {
        "data": []
      },
      "inboxes": {
        "data": [
          {
            "id": "13",
            "type": "inbox",
            "attributes": {
              "name": "HackerOne",
              "type": "default"
            }
          },
          {
            "id": "65",
            "type": "inbox",
            "attributes": {
              "name": "Custom Inbox number one",
              "type": "custom"
            }
          }
        ]
      },
      "triggered_pre_submission_trigger": {
        "data": {
          "id": "1337",
          "type": "trigger",
          "attributes": {
            "title": "Example Trigger"
          }
        }
      },
      "custom_field_values": {
        "data": []
      },
      "automated_remediation_guidance": {
        "data": {
          "id": "1",
          "type": "automated-remediation-guidance",
          "attributes": {
            "reference": "https://cwe.mitre.org/data/definitions/120.html",
            "created_at": "2020-10-23T12:09:37.859Z"
          }
        }
      },
      "custom_remediation_guidance": {
        "data": {
          "id": "84",
          "type": "custom-remediation-guidance",
          "attributes": {
            "message": "Check buffer boundaries if accessing the buffer in a loop and make sure you are not in danger of writing past the allocated space.",
            "created_at": "2020-10-26T08:47:23.296Z"
          },
          "relationships": {
            "author": {
              "data": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api-example-2",
                  "name": "API Example 2",
                  "disabled": false,
                  "created_at": "2020-10-22T011:22:05.402Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Last revised: 2025-12-16

`DELETE /reports/{report_id}/escalate`

This API endpoint can be used to remove an escalation from a report. When the request is successful, the API will respond with a success message.

Required permission: Report Management. You can manage the permissions of your API users through your program's settings. Insufficient permissions will result in a 403 Forbidden response.

Trying to remove an escalation with an invalid report ID or without proper authorization will return appropriate error messages.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| report_id | path | integer | true | The ID of the report. |

### Update Report Tags

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/report_tags" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-tags",
    "attributes": {
      "report_tags": [
        "string"
      ]
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-tags",
    "attributes": {
      "report_tags": [
        "string"
      ]
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/report_tags',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-tags",
    "attributes": {
      "report_tags": [
        "string"
      ]
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/report_tags',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/report_tags");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-tags\",\n    \"attributes\": {\n      \"report_tags\": [\n        \"string\"\n      ]\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-tags\",\n    \"attributes\": {\n      \"report_tags\": [\n        \"string\"\n      ]\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/report_tags',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-tags\",\n    \"attributes\": {\n      \"report_tags\": [\n        \"string\"\n      ]\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/report_tags", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Report tags updated

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "main_state": "open",
    "state": "new",
    "created_at": "2024-01-20T14:26:19.286Z",
    "submitted_at": "2024-01-20T14:26:19.286Z",
    "vulnerability_information": "Vuln information",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "reporter_agreed_on_going_public_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "cve_ids": [],
    "source": null,
    "timer_bounty_awarded_elapsed_time": null,
    "timer_bounty_awarded_miss_at": null,
    "timer_first_program_response_miss_at": null,
    "timer_first_program_response_elapsed_time": null,
    "timer_report_resolved_miss_at": null,
    "timer_report_resolved_elapsed_time": null,
    "timer_report_triage_miss_at": null,
    "timer_report_triage_elapsed_time": null,
    "report_tags": [
      "urgent"
    ]
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "bio": null,
          "website": null,
          "location": null,
          "hackerone_triager": false
        }
      }
    },
    "collaborators": {
      "data": []
    },
    "assignee": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "member",
          "name": "Member",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "signal": null,
          "impact": null,
          "reputation": null,
          "bio": null,
          "website": null,
          "location": null,
          "hackerone_triager": false
        }
      }
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "activities": {
      "data": [
        {
          "type": "activity-cve-id-added",
          "id": "445",
          "attributes": {
            "message": "",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z",
            "internal": false
          },
          "relationships": {
            "actor": {
              "data": {
                "id": "1337",
                "type": "user",
                "attributes": {
                  "username": "member",
                  "name": "Member",
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  },
                  "signal": null,
                  "impact": null,
                  "reputation": null,
                  "bio": null,
                  "website": null,
                  "location": null,
                  "hackerone_triager": false
                }
              }
            }
          }
        }
      ]
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    },
    "inboxes": {
      "data": []
    },
    "custom_field_values": {
      "data": []
    }
  }
}

```

Last revised: 2026-03-17

`PUT /reports/{id}/report_tags`

This endpoint allows you to update tags associated with a report. The provided tags will replace all existing tags on the report (not append to them).

Required permissions: Report Management. Configure API user permissions through your organization's settings. Users with insufficient permissions will receive a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the tags on a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» report_tags | body | [string] | true | The names of the tags on the report. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-tags |

### Request Retest

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/retests" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "retest_award_amount": null
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "retest_award_amount": null
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/retests',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "retest_award_amount": null
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/retests',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/retests");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"retest_award_amount\": null\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"retest_award_amount\": null\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/retests',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"retest_award_amount\": null\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/retests", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report retest requested

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-03-10

`POST /reports/{id}/retests`

Requesting a retest for a report can be done through this endpoint.

The parameter`retest_award_amount` is only required for Bug Bounty Programs (BBPs) and Challenges when the team's retest subscription allows awarding hackers. For Vulnerability Disclosure Programs (VDPs), Pentests and other types engagements, this field is not required. This field should not be included in the request or should have a`null` value.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to request retesting on a report. |
| » type | body | string | true | none |
| » attributes | body | object | false | none |
| »» message | body | string | false | The message that will be posted. |
| »» retest_award_amount | body | float | false | The award amount to be awarded to the retester. Required only for BBPs and Challenges, when the team's retest subscription allows awarding hackers. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | retest |

### Approve Retest

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/retests/approve" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "award_amount": null
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "award_amount": null
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/retests/approve',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string",
      "award_amount": null
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/retests/approve',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/retests/approve");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"award_amount\": null\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"award_amount\": null\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/retests/approve',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"award_amount\": null\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/retests/approve", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

retest approved

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-03-10

`POST /reports/{id}/retests/approve`

Approve a completed retest for a report. This marks the retest as resolved — the bug has been fixed by the hacker — and closes the report.

The parameter`award_amount` is only required for Bug Bounty Programs (BBPs) when the team's retest subscription allows awarding hackers. For VDPs, Pentests and other engagement types, this field is not required.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to approve a retest on a report. |
| » type | body | string | true | none |
| » attributes | body | object | false | none |
| »» message | body | string | false | Optional message to the hacker upon approval. |
| »» award_amount | body | float | false | The award amount to be awarded to the retester. Required only for BBPs when the team's retest subscription allows awarding hackers. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | retest |

### Reject Retest

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/retests/reject" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/retests/reject',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/retests/reject',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/retests/reject");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/retests/reject',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/retests/reject", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

retest rejected

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-03-10

`POST /reports/{id}/retests/reject`

Reject a completed retest for a report. This marks the retest as not properly performed and reverts the report to its previous state. A message explaining why the retest was rejected is required.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to reject a retest on a report. |
| » type | body | string | true | none |
| » attributes | body | object | false | none |
| »» message | body | string | true | Required message explaining why the retest was rejected. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | retest |

### Cancel Retest

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/retests/cancel" \
  -X DELETE \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}

r = requests.delete(
  'https://api.hackerone.com/v1/reports/{id}/retests/cancel',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "retest",
    "attributes": {
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :delete,
  url: 'https://api.hackerone.com/v1/reports/{id}/retests/cancel',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/retests/cancel");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("DELETE");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/retests/cancel',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"retest\",\n    \"attributes\": {\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("DELETE", "https://api.hackerone.com/v1/reports/{id}/retests/cancel", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report retest canceled

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-03-10

`DELETE /reports/{id}/retests/cancel`

Cancel a retest for a report through this endpoint. This will cancel the ongoing retest and revert the report to its previous state.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to cancel a retest on a report. |
| » type | body | string | true | none |
| » attributes | body | object | false | none |
| »» message | body | string | false | Optional message explaining the reason for cancellation. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | retest |

### Update Severity

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/severities" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "severity",
    "attributes": {
      "rating": "none",
      "attack_vector": "network",
      "attack_complexity": "low",
      "attack_requirements": "none",
      "privileges_required": "none",
      "user_interaction": "none",
      "scope": "unchanged",
      "confidentiality": "none",
      "integrity": "none",
      "availability": "none",
      "vulnerable_confidentiality": "none",
      "vulnerable_integrity": "none",
      "vulnerable_availability": "none",
      "subsequent_confidentiality": "none",
      "subsequent_integrity": "none",
      "subsequent_availability": "none",
      "calculation_method": "cvss_3_0_hackerone",
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "severity",
    "attributes": {
      "rating": "none",
      "attack_vector": "network",
      "attack_complexity": "low",
      "attack_requirements": "none",
      "privileges_required": "none",
      "user_interaction": "none",
      "scope": "unchanged",
      "confidentiality": "none",
      "integrity": "none",
      "availability": "none",
      "vulnerable_confidentiality": "none",
      "vulnerable_integrity": "none",
      "vulnerable_availability": "none",
      "subsequent_confidentiality": "none",
      "subsequent_integrity": "none",
      "subsequent_availability": "none",
      "calculation_method": "cvss_3_0_hackerone",
      "message": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/severities',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "severity",
    "attributes": {
      "rating": "none",
      "attack_vector": "network",
      "attack_complexity": "low",
      "attack_requirements": "none",
      "privileges_required": "none",
      "user_interaction": "none",
      "scope": "unchanged",
      "confidentiality": "none",
      "integrity": "none",
      "availability": "none",
      "vulnerable_confidentiality": "none",
      "vulnerable_integrity": "none",
      "vulnerable_availability": "none",
      "subsequent_confidentiality": "none",
      "subsequent_integrity": "none",
      "subsequent_availability": "none",
      "calculation_method": "cvss_3_0_hackerone",
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/severities',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/severities");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"severity\",\n    \"attributes\": {\n      \"rating\": \"none\",\n      \"attack_vector\": \"network\",\n      \"attack_complexity\": \"low\",\n      \"attack_requirements\": \"none\",\n      \"privileges_required\": \"none\",\n      \"user_interaction\": \"none\",\n      \"scope\": \"unchanged\",\n      \"confidentiality\": \"none\",\n      \"integrity\": \"none\",\n      \"availability\": \"none\",\n      \"vulnerable_confidentiality\": \"none\",\n      \"vulnerable_integrity\": \"none\",\n      \"vulnerable_availability\": \"none\",\n      \"subsequent_confidentiality\": \"none\",\n      \"subsequent_integrity\": \"none\",\n      \"subsequent_availability\": \"none\",\n      \"calculation_method\": \"cvss_3_0_hackerone\",\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"severity\",\n    \"attributes\": {\n      \"rating\": \"none\",\n      \"attack_vector\": \"network\",\n      \"attack_complexity\": \"low\",\n      \"attack_requirements\": \"none\",\n      \"privileges_required\": \"none\",\n      \"user_interaction\": \"none\",\n      \"scope\": \"unchanged\",\n      \"confidentiality\": \"none\",\n      \"integrity\": \"none\",\n      \"availability\": \"none\",\n      \"vulnerable_confidentiality\": \"none\",\n      \"vulnerable_integrity\": \"none\",\n      \"vulnerable_availability\": \"none\",\n      \"subsequent_confidentiality\": \"none\",\n      \"subsequent_integrity\": \"none\",\n      \"subsequent_availability\": \"none\",\n      \"calculation_method\": \"cvss_3_0_hackerone\",\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/severities',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"severity\",\n    \"attributes\": {\n      \"rating\": \"none\",\n      \"attack_vector\": \"network\",\n      \"attack_complexity\": \"low\",\n      \"attack_requirements\": \"none\",\n      \"privileges_required\": \"none\",\n      \"user_interaction\": \"none\",\n      \"scope\": \"unchanged\",\n      \"confidentiality\": \"none\",\n      \"integrity\": \"none\",\n      \"availability\": \"none\",\n      \"vulnerable_confidentiality\": \"none\",\n      \"vulnerable_integrity\": \"none\",\n      \"vulnerable_availability\": \"none\",\n      \"subsequent_confidentiality\": \"none\",\n      \"subsequent_integrity\": \"none\",\n      \"subsequent_availability\": \"none\",\n      \"calculation_method\": \"cvss_3_0_hackerone\",\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/severities", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

severity updated

```
{
  "id": "57",
  "type": "severity",
  "attributes": {
    "rating": "low",
    "author_type": "User",
    "user_id": 1337,
    "created_at": "2023-11-21T14:00:16.142Z",
    "score": 3.9,
    "attack_complexity": "low",
    "attack_vector": "network",
    "confidentiality": "low",
    "integrity": "low",
    "availability": "low",
    "privileges_required": "low",
    "user_interaction": "required",
    "scope": "changed",
    "confidentiality_requirement": "medium",
    "integrity_requirement": "low",
    "availability_requirement": "low",
    "max_severity": "low",
    "calculation_method": "cvss_3_1",
    "cvss_vector_string": "CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:L"
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/severities`

You can use this endpoint to create or update the severity of the provided report. If the report already has a severity, a new one will be created and used as the current severity. You have to provide either rating or metrics of the vulnerability severity.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the severity of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» rating | body | [severity-ratings](https://api.hackerone.com/customer-reference#severity-ratings) | false | The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score. |
| »» attack_vector | body | string¦null | false | A CVSS metric that reflects the context by which vulnerability exploritation is possible. |
| »» attack_complexity | body | string | false | A CVSS metric that describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability. |
| »» attack_requirements | body | string | false | A CVSS metric that captures the prerequisite deployment and execution conditions or variables of the vulnerable system that enable the attack. |
| »» privileges_required | body | string | false | A CVSS metric that describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. |
| »» user_interaction | body | string | false | A CVSS metric that captures the requirement for a user, other than the attacker, to participate in the successful compromise of the vulnerability component. |
| »» scope | body | string¦null | false | A CVSS metric that determines if a successful attack impacts a component other than the vulnerable component. |
| »» confidentiality | body | string | false | A CVSS metric that measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. |
| »» integrity | body | string | false | A CVSS metric that measures the impact to the integrity of a successfully exploited vulnerability. |
| »» availability | body | string | false | A CVSS metric that measures the availability of the impacted component resulting from a successfully exploited vulnerability. |
| »» vulnerable_confidentiality | body | string | false | A CVSS metric that measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. |
| »» vulnerable_integrity | body | string | false | This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity refers to the trustworthiness and veracity of information. |
| »» vulnerable_availability | body | string | false | This metric measures the impact to the availability of the impacted system resulting from a successfully exploited vulnerability. |
| »» subsequent_confidentiality | body | string | false | This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability of subsequent systems. |
| »» subsequent_integrity | body | string | false | This metric measures the impact to integrity of a successfully exploited vulnerability of subsequent systems. Integrity refers to the trustworthiness and veracity of information. |
| »» subsequent_availability | body | string | false | This metric measures the impact to the availability of the impacted system resulting from a successfully exploited vulnerability of subsequent systems. |
| »» calculation_method | body | string | false | The method used to calculate the severity of the vulnerability. |
| »» message | body | string | false | A message to be added to the severity. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | severity |
| »» rating | none |
| »» rating | low |
| »» rating | medium |
| »» rating | high |
| »» rating | critical |
| »» attack_vector | network |
| »» attack_vector | adjacent |
| »» attack_vector | local |
| »» attack_vector | physical |
| »» attack_complexity | low |
| »» attack_complexity | high |
| »» attack_requirements | none |
| »» attack_requirements | present |
| »» privileges_required | none |
| »» privileges_required | low |
| »» privileges_required | high |
| »» user_interaction | none |
| »» user_interaction | required |
| »» scope | unchanged |
| »» scope | changed |
| »» confidentiality | none |
| »» confidentiality | low |
| »» confidentiality | high |
| »» integrity | none |
| »» integrity | low |
| »» integrity | high |
| »» availability | none |
| »» availability | low |
| »» availability | high |
| »» vulnerable_confidentiality | none |
| »» vulnerable_confidentiality | low |
| »» vulnerable_confidentiality | high |
| »» vulnerable_integrity | none |
| »» vulnerable_integrity | low |
| »» vulnerable_integrity | high |
| »» vulnerable_availability | none |
| »» vulnerable_availability | low |
| »» vulnerable_availability | high |
| »» subsequent_confidentiality | none |
| »» subsequent_confidentiality | low |
| »» subsequent_confidentiality | high |
| »» subsequent_integrity | none |
| »» subsequent_integrity | low |
| »» subsequent_integrity | high |
| »» subsequent_availability | none |
| »» subsequent_availability | low |
| »» subsequent_availability | high |
| »» calculation_method | cvss_3_0_hackerone |
| »» calculation_method | cvss_3_1 |
| »» calculation_method | cvss_4_0 |
| »» calculation_method | manual |

### Change State

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/state_changes" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "state-change",
    "attributes": {
      "message": "string",
      "state": "new",
      "original_report_id": 0,
      "attachment_ids": []
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "state-change",
    "attributes": {
      "message": "string",
      "state": "new",
      "original_report_id": 0,
      "attachment_ids": []
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/state_changes',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "state-change",
    "attributes": {
      "message": "string",
      "state": "new",
      "original_report_id": 0,
      "attachment_ids": []
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/state_changes',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/state_changes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"state-change\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"state\": \"new\",\n      \"original_report_id\": 0,\n      \"attachment_ids\": []\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"state-change\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"state\": \"new\",\n      \"original_report_id\": 0,\n      \"attachment_ids\": []\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/state_changes',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"state-change\",\n    \"attributes\": {\n      \"message\": \"string\",\n      \"state\": \"new\",\n      \"original_report_id\": 0,\n      \"attachment_ids\": []\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/state_changes", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report state changed

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2025-06-20

`POST /reports/{id}/state_changes`

Changing the state of a report can be done through this endpoint. Closing a report as resolved will automatically recognize the finder in the program's hall of fame and reputation will be given. If a report is closed as N/A, Informative, or Spam, reputation will be deducted from the finder's track record.

There is currently 1 feature missing in the state change API: the ability to invite the finder of the duplicate to the original report. This feature will be implemented in a future version of the API.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Allowed state transitions:

| Old value | New value |
| --- | --- |
| duplicate | new, triaged |
| editing | deleted, needs-more-info, new, not-applicable |
| informative | new, triaged |
| needs-more-info | duplicate, informative, new, not-applicable, pending-program-review, resolved, spam, triaged |
| new | duplicate, informative, needs-more-info, not-applicable, pending-program-review, resolved, spam, triaged |
| not-applicable | new, triaged |
| pending-program-review | duplicate, informative, needs-more-info, new, not-applicable, resolved, spam, triaged |
| needs-more-info, new, not-applicable |
| resolved | new, triaged |
| spam | new, triaged |
| triaged | duplicate, informative, needs-more-info, new, not-applicable, pending-program-review, resolved, spam, triaged |

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the state of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» message | body | string | true | The message that will be posted. Required when the new state is needs-more-info, informative, or duplicate. |
| »» state | body | [report-states](https://api.hackerone.com/customer-reference#report-states) | true | none |
| »» original_report_id | body | integer | false | The ID of the report to use as the original report. Only available when closing the report as duplicate. |
| »» attachment_ids | body | array | false | Array of attachment IDs. You can upload attachments [here](https://api.hackerone.com/customer-resources/#reports-upload-attachments) |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | state-change |
| »» state | new |
| »» state | pending-program-review |
| »» state | triaged |
| »» state | needs-more-info |
| »» state | resolved |
| »» state | not-applicable |
| »» state | informative |
| »» state | duplicate |
| »» state | spam |
| »» state | retesting |

### Update Structured Scope

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/structured_scope" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-structured-scope",
    "attributes": {
      "structured_scope_id": 0
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-structured-scope",
    "attributes": {
      "structured_scope_id": 0
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/structured_scope',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-structured-scope",
    "attributes": {
      "structured_scope_id": 0
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/structured_scope',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/structured_scope");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-structured-scope\",\n    \"attributes\": {\n      \"structured_scope_id\": 0\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-structured-scope\",\n    \"attributes\": {\n      \"structured_scope_id\": 0\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/structured_scope',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-structured-scope\",\n    \"attributes\": {\n      \"structured_scope_id\": 0\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/structured_scope", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

Updated structured scope

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/structured_scope`

Changing the structured scope of a report can be done through this endpoint. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the structured scope of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» structured_scope_id | body | integer | true | The new structured scope that will be set on the report. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-structured-scope |

### Add Summary

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/summaries" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-summary",
    "attributes": {
      "content": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-summary",
    "attributes": {
      "content": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/summaries',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-summary",
    "attributes": {
      "content": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/summaries',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/summaries");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-summary\",\n    \"attributes\": {\n      \"content\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-summary\",\n    \"attributes\": {\n      \"content\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/summaries',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-summary\",\n    \"attributes\": {\n      \"content\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/summaries", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

summary created

```
{
  "id": "1337",
  "type": "report-summary",
  "attributes": {
    "content": "There was a cross-site scripting vulnerability in our login form.",
    "category": "team",
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "attachments": {
      "data": []
    },
    "user": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/summaries`

This API endpoint enables the user to create a report summary for reports that are received by teams that the user is a part of.

A team can only include a single report summary. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform or reported to other teams.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information necessary to create a report summary. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» content | body | string | true | The content to be included in the report summary. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-summary |

### Award Swag

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/swags" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "message": "string"
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "message": "string"
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/swags',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "message": "string"
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/swags',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/swags");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"message\": \"string\"\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"message\": \"string\"\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/swags',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"message\": \"string\"\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/swags", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

swag awarded

```
{
  "id": "1337",
  "type": "swag",
  "attributes": {
    "sent": false,
    "created_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "user": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    },
    "address": {
      "data": {
        "id": "1337",
        "type": "address",
        "attributes": {
          "name": "Jane Doe",
          "street": "535 Mission Street",
          "city": "San Francisco",
          "postal_code": "94105",
          "state": "CA",
          "country": "United States of America",
          "created_at": "2016-02-02T04:05:06.000Z",
          "tshirt_size": "W_Large",
          "phone_number": "+1-510-000-0000"
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`POST /reports/{id}/swags`

You can use this endpoint to award swag to the reporter of the provided report.

Required permissions: Reward Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information required to award swag. |
| » message | body | string | true | The public message posted on the report. This is always required. |

### Update Title

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/title" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-title",
    "attributes": {
      "title": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-title",
    "attributes": {
      "title": "string"
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/title',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-title",
    "attributes": {
      "title": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/title',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/title");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-title\",\n    \"attributes\": {\n      \"title\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-title\",\n    \"attributes\": {\n      \"title\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/title',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-title\",\n    \"attributes\": {\n      \"title\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/title", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

title updated

```
{
  "data": {
    "id": "1337",
    "type": "report",
    "attributes": {
      "title": "XSS in login form",
      "state": "new",
      "created_at": "2016-02-02T04:05:06.000Z",
      "vulnerability_information": "...",
      "triaged_at": null,
      "closed_at": null,
      "last_reporter_activity_at": null,
      "first_program_activity_at": null,
      "last_program_activity_at": null,
      "bounty_awarded_at": null,
      "swag_awarded_at": null,
      "disclosed_at": null,
      "source": null
    },
    "relationships": {
      "reporter": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "collaborators": {
        "data": [
          {
            "weight": 1,
            "user": {
              "id": "1337",
              "type": "user",
              "attributes": {
                "username": "api-example",
                "name": "API Example",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          },
          {
            "weight": 1,
            "user": {
              "id": "1338",
              "type": "user",
              "attributes": {
                "username": "api-example 2",
                "name": "API Example 2",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          }
        ]
      },
      "assignee": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "member",
            "name": "Member",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "program": {
        "data": {
          "id": "1337",
          "type": "program",
          "attributes": {
            "handle": "security",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "severity": {
        "data": {
          "id": "57",
          "type": "severity",
          "attributes": {
            "rating": "high",
            "author_type": "User",
            "user_id": 1337,
            "created_at": "2016-02-02T04:05:06.000Z",
            "score": 8.7,
            "attack_complexity": "low",
            "attack_vector": "adjacent",
            "availability": "high",
            "confidentiality": "low",
            "integrity": "high",
            "privileges_required": "low",
            "user_interaction": "required",
            "scope": "changed"
          }
        }
      },
      "swag": {
        "data": []
      },
      "attachments": {
        "data": []
      },
      "weakness": {
        "data": {
          "id": "1337",
          "type": "weakness",
          "attributes": {
            "name": "Cross-Site Request Forgery (CSRF)",
            "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
            "external_id": "cwe-352",
            "created_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "structured_scope": {
        "data": {
          "id": "57",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "url",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2015-02-02T04:05:06.000Z",
            "updated_at": "2016-05-02T04:05:06.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      },
      "campaign": null,
      "activities": {
        "data": [
          {
            "type": "activity-comment",
            "id": "445",
            "attributes": {
              "message": "Comment!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    },
                    "signal": null,
                    "impact": null,
                    "reputation": null,
                    "bio": null,
                    "website": null,
                    "location": null,
                    "hackerone_triager": false
                  }
                }
              },
              "attachments": {
                "data": [
                  {
                    "id": "1337",
                    "type": "attachment",
                    "attributes": {
                      "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
                      "created_at": "2016-02-02T04:05:06.000Z",
                      "file_name": "root.rb",
                      "content_type": "text/x-ruby",
                      "file_size": 2871
                    }
                  }
                ]
              }
            }
          },
          {
            "id": "1337",
            "type": "activity-bug-resolved",
            "attributes": {
              "message": "Bug Resolved!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    }
                  }
                }
              }
            }
          }
        ]
      },
      "bounties": {
        "data": []
      },
      "summaries": {
        "data": []
      },
      "inboxes": {
        "data": [
          {
            "id": "13",
            "type": "inbox",
            "attributes": {
              "name": "HackerOne",
              "type": "default"
            }
          },
          {
            "id": "65",
            "type": "inbox",
            "attributes": {
              "name": "Custom Inbox number one",
              "type": "custom"
            }
          }
        ]
      },
      "triggered_pre_submission_trigger": {
        "data": {
          "id": "1337",
          "type": "trigger",
          "attributes": {
            "title": "Example Trigger"
          }
        }
      },
      "custom_field_values": {
        "data": []
      },
      "automated_remediation_guidance": {
        "data": {
          "id": "1",
          "type": "automated-remediation-guidance",
          "attributes": {
            "reference": "https://cwe.mitre.org/data/definitions/120.html",
            "created_at": "2020-10-23T12:09:37.859Z"
          }
        }
      },
      "custom_remediation_guidance": {
        "data": {
          "id": "84",
          "type": "custom-remediation-guidance",
          "attributes": {
            "message": "Check buffer boundaries if accessing the buffer in a loop and make sure you are not in danger of writing past the allocated space.",
            "created_at": "2020-10-26T08:47:23.296Z"
          },
          "relationships": {
            "author": {
              "data": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api-example-2",
                  "name": "API Example 2",
                  "disabled": false,
                  "created_at": "2020-10-22T011:22:05.402Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/title`

Changing the title of a report through the HackerOne API can be useful to programmatically batch update received reports in HackerOne. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Report or Program Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the title of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» title | body | string | true | The new title that will be set on the report. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-title |

### Transfer Report

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/transfer" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-transfer",
    "attributes": {
      "target_team_id": 0,
      "no_notifications": true
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-transfer",
    "attributes": {
      "target_team_id": 0,
      "no_notifications": true
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/transfer',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-transfer",
    "attributes": {
      "target_team_id": 0,
      "no_notifications": true
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/transfer',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/transfer");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-transfer\",\n    \"attributes\": {\n      \"target_team_id\": 0,\n      \"no_notifications\": true\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-transfer\",\n    \"attributes\": {\n      \"target_team_id\": 0,\n      \"no_notifications\": true\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/transfer',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-transfer\",\n    \"attributes\": {\n      \"target_team_id\": 0,\n      \"no_notifications\": true\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/transfer", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report transferred

```
{
  "was_successful": true
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/transfer`

The program can transfer reports between parent and child programs.

You can use this endpoint to transfer the reports between parent and child programs.

IMPORTANT: When transferring reports references are being removed. Custom field values will also be removed, unless a custom field with the exact same label exists on the target team.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to transfer the report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» target_team_id | body | number | true | ID of the target team the reports should be transferred to. |
| »» no_notifications | body | boolean | false | If the action should create notifications. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-transfer |

### Update Weakness

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/weakness" \
  -X PUT \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report-weakness",
    "attributes": {
      "weakness_id": 0
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report-weakness",
    "attributes": {
      "weakness_id": 0
    }
  }
}

r = requests.put(
  'https://api.hackerone.com/v1/reports/{id}/weakness',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report-weakness",
    "attributes": {
      "weakness_id": 0
    }
  }
}

result = RestClient::Request.execute(
  method: :put,
  url: 'https://api.hackerone.com/v1/reports/{id}/weakness',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/weakness");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("PUT");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report-weakness\",\n    \"attributes\": {\n      \"weakness_id\": 0\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report-weakness\",\n    \"attributes\": {\n      \"weakness_id\": 0\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/weakness',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report-weakness\",\n    \"attributes\": {\n      \"weakness_id\": 0\n    }\n  }\n}"`))

    req, err := http.NewRequest("PUT", "https://api.hackerone.com/v1/reports/{id}/weakness", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

assignee updated

```
{
  "id": "77",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2019-08-20T14:26:19.286Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": "2019-08-20T14:26:20.531Z",
    "first_program_activity_at": "2019-08-20T14:26:20.531Z",
    "last_program_activity_at": "2019-08-20T15:25:56.627Z",
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": "2019-08-20T15:25:56.627Z",
    "last_activity_at": "2019-08-20T15:25:56.627Z",
    "cve_ids": []
  },
  "relationships": {
    "weakness": {
      "data": {
        "id": "77",
        "type": "weakness",
        "attributes": {
          "name": "Reliance on Reverse DNS Resolution for a Security-Critical Action",
          "description": "The software performs reverse DNS resolution on an IP address to obtain the hostname and make a security decision, but it does not properly ensure that the IP address is truly associated with the hostname.",
          "external_id": "cwe-350",
          "created_at": "2019-07-12T08:36:13.646Z"
        }
      }
    }
  }
}

```

Last revised: 2025-05-23

`PUT /reports/{id}/weakness`

Changing the weakness of a report can be done through this endpoint. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 404 Not Found response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to change the weakness of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» weakness_id | body | integer | true | The new weakness that will be set on the report. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report-weakness |

### Get All Reports

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/reports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/reports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/reports", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

ignores filter and returns all reports when feature disabled

```
{
  "data": [
    {
      "id": "1337",
      "type": "report",
      "attributes": {
        "title": "XSS in login form",
        "state": "new",
        "created_at": "2016-02-02T04:05:06.000Z",
        "submitted_at": "2016-02-04T04:05:06.000Z",
        "vulnerability_information": "...",
        "triaged_at": null,
        "closed_at": null,
        "last_reporter_activity_at": null,
        "first_program_activity_at": null,
        "last_program_activity_at": null,
        "bounty_awarded_at": null,
        "last_activity_at": null,
        "last_public_activity_at": null,
        "swag_awarded_at": null,
        "disclosed_at": null
      },
      "relationships": {
        "reporter": {
          "data": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "collaborators": {
          "data": [
            {
              "weight": 1,
              "user": {
                "id": "1337",
                "type": "user",
                "attributes": {
                  "username": "api-example",
                  "name": "API Example",
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  },
                  "reputation": 7,
                  "signal": 7,
                  "impact": 30
                }
              }
            },
            {
              "weight": 1,
              "user": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api-example 2",
                  "name": "API Example 2",
                  "disabled": false,
                  "created_at": "2016-02-02T04:05:06.000Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  },
                  "reputation": 7,
                  "signal": 7,
                  "impact": 30
                }
              }
            }
          ]
        },
        "program": {
          "data": {
            "id": "1337",
            "type": "program",
            "attributes": {
              "handle": "security",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z"
            }
          }
        },
        "weakness": {
          "data": {
            "id": "1337",
            "type": "weakness",
            "attributes": {
              "name": "Cross-Site Request Forgery (CSRF)",
              "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
              "external_id": "cwe-352",
              "created_at": "2016-02-02T04:05:06.000Z"
            }
          }
        },
        "bounties": {
          "data": []
        }
      }
    },
    {
      "id": "1338",
      "type": "report",
      "attributes": {
        "title": "CSRF in admin panel",
        "state": "triaged",
        "created_at": "2016-02-02T04:05:06.000Z",
        "submitted_at": "2016-02-04T04:05:06.000Z",
        "vulnerability_information": "...",
        "triaged_at": "2016-02-03T03:01:36.000Z",
        "closed_at": null,
        "last_reporter_activity_at": null,
        "first_program_activity_at": null,
        "last_program_activity_at": null,
        "bounty_awarded_at": null,
        "swag_awarded_at": null,
        "disclosed_at": null,
        "issue_tracker_reference_id": "T554",
        "issue_tracker_reference_url": "https://phabricator.tld/T554",
        "cve_ids": []
      },
      "relationships": {
        "reporter": {
          "data": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              }
            }
          }
        },
        "program": {
          "data": {
            "id": "1337",
            "type": "program",
            "attributes": {
              "handle": "security",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z"
            }
          }
        },
        "weakness": {
          "data": {
            "id": "1337",
            "type": "weakness",
            "attributes": {
              "name": "Cross-Site Request Forgery (CSRF)",
              "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
              "external_id": "cwe-352",
              "created_at": "2016-02-02T04:05:06.000Z"
            }
          }
        },
        "bounties": {
          "data": []
        },
        "inboxes": {
          "data": [
            {
              "id": "13",
              "type": "inbox",
              "attributes": {
                "name": "Security Program Inbox",
                "type": "default"
              }
            },
            {
              "id": "79",
              "type": "inbox",
              "attributes": {
                "name": "Custom Inbox",
                "type": "custom"
              }
            }
          ]
        }
      }
    },
    "..."
  ],
  "links": {
    "self": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=1",
    "next": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=2",
    "last": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=5"
  }
}

```

Last revised: 2026-04-14

`GET /reports`

Multiple report objects can be queried that meet certain filtering criteria by sending a GET request to the reports endpoint. When the request is successful, the API will respond with paginated [report objects](https://api.hackerone.com/customer-reference#report).

IMPORTANT: Either the filter parameter`program` or`inbox_ids` is required when using this endpoint.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filter[program][] | query | array[string] | false | Filter by the program handles you want to fetch the reports for. Required if`inbox_ids` is not specified. |
| filter[inbox_ids][] | query | array[integer] | false | Filter by the inbox ids you want to fetch the reports for. Required if`program` is not specified. |
| filter[reporter][] | query | array[string] | false | Filter by the hacker's username you want to fetch the reports for. |
| filter[assignee][] | query | array[string] | false | Filter by the assignee's usernames, emails or group names you want to fetch the reports for. |
| filter[state][] | query | array[string] | false | Filter by current report state. |
| filter[id][] | query | array[integer] | false | Filter by report ID. |
| filter[weakness_id][] | query | array[integer] | false | Filter by weakness. |
| filter[severity][] | query | array[string] | false | Filter by the severity ratings you want to fetch the reports for. |
| filter[asset_ids][] | query | array[integer] | false | Filter by the asset ids you want to fetch the reports for. |
| filter[hacker_published] | query | boolean | false | Filter by reports that are published by hackers, depending on the value of the parameter. |
| filter[hai_is_priority] | query | boolean | false | Filter by reports flagged as priority by the Prioritization Agent. When true, returns only priority reports. When false, returns only non-priority reports. This field is only populated for reports with priority recommendation data and on Enterprise product editions. |
| filter[created_at__gt] | query | any(date-time) | false | Filter by reports that were created after the date specified. |
| filter[created_at__lt] | query | any(date-time) | false | Filter by reports that were created before the date specified. |
| filter[submitted_at__gt] | query | any(date-time) | false | Filter by reports that were submitted after the date specified. |
| filter[submitted_at__lt] | query | any(date-time) | false | Filter by reports that were submitted before the date specified. |
| filter[triaged_at__gt] | query | any(date-time) | false | Filter by reports that were triaged after the date specified. |
| filter[triaged_at__lt] | query | any(date-time) | false | Filter by reports that were triaged before the date specified. |
| filter[triaged_at__null] | query | boolean | false | Filter by reports that are triaged or not, depending on the value of this parameter. |
| filter[closed_at__gt] | query | any(date-time) | false | Filter by reports that were closed after the date specified. |
| filter[closed_at__lt] | query | any(date-time) | false | Filter by reports that were closed before the date specified. |
| filter[closed_at__null] | query | boolean | false | Filter by reports that are closed or not, depending on the value of this parameter. |
| filter[disclosed_at__gt] | query | any(date-time) | false | Filter by reports that were disclosed after the date specified. |
| filter[disclosed_at__lt] | query | any(date-time) | false | Filter by reports that were disclosed before the date specified. |
| filter[disclosed_at__null] | query | boolean | false | Filter by reports that are disclosed. |
| filter[reporter_agreed_on_going_public] | query | boolean | false | Filter by reports that have the hacker disclosure request. |
| filter[bounty_awarded_at__gt] | query | any(date-time) | false | Filter by reports that have a bounty awarded after the date specified. |
| filter[bounty_awarded_at__lt] | query | any(date-time) | false | Filter by reports that have a bounty awarded before the date specified. |
| filter[bounty_awarded_at__null] | query | boolean | false | Filter by reports that have a bounty awarded. |
| filter[swag_awarded_at__gt] | query | any(date-time) | false | Filter by reports that have swag awarded after the date specified. |
| filter[swag_awarded_at__lt] | query | any(date-time) | false | Filter by reports that have swag awarded before the date specified. |
| filter[swag_awarded_at__null] | query | boolean | false | Filter by reports that have swag awarded or not, depending on the value of this parameter. |
| filter[last_reporter_activity_at__gt] | query | any(date-time) | false | Filter by reports that received an update from the reporter after the date specified. |
| filter[last_reporter_activity_at__lt] | query | any(date-time) | false | Filter by reports that received an update from the reporter before the date specified. |
| filter[first_program_activity_at__gt] | query | any(date-time) | false | Filter by reports that received the first update from the program after the date specified. |
| filter[first_program_activity_at__lt] | query | any(date-time) | false | Filter by reports that received the first update from the program before the date specified. |
| filter[first_program_activity_at__null] | query | boolean | false | Filter by reports where the reporter received an update. |
| filter[last_program_activity_at__gt] | query | any(date-time) | false | Filter by reports that received an update from the program after the date specified. |
| filter[last_program_activity_at__lt] | query | any(date-time) | false | Filter by reports that received an update from the program before the date specified. |
| filter[last_activity_at__gt] | query | any(date-time) | false | Filter by reports that received an update after the date specified. |
| filter[last_activity_at__lt] | query | any(date-time) | false | Filter by reports that received an update before the date specified. |
| filter[last_public_activity_at__gt] | query | any(date-time) | false | Filter by reports that received a public update after the date specified. |
| filter[last_public_activity_at__lt] | query | any(date-time) | false | Filter by reports that received a public update after the date specified. |
| filter[keyword] | query | string | false | Filter reports by title and keywords. |
| filter[issue_tracker_reference_id] | query | string | false | Filter reports by issue tracker reference. |
| filter[issue_tracker_reference_id__null] | query | boolean | false | Filter by reports that have an issue tracker reference or not, depending on the value of this parameter. |
| filter[custom_fields][] | query | array[object] | false | Filter reports by a Custom Field Label and Value. See [custom-field-input](https://api.hackerone.com/customer-reference#custom-field-input) for an exampleof the input values |
| sort | query | any | false | The attributes and order to sort the reports on. |
| page[number] | query | integer | false | The page to retrieve from. The default is set to 1. |
| page[size] | query | integer | false | The number of objects per page (currently limited from 1 to 100). The default is set to 25. |

Detailed descriptions

sort: The attributes and order to sort the reports on.

This parameter may contain multiple attributes that the reports should be sorted on. Sorting is applied in the specified order of attributes. If an attribute should be sorted descending, prepend a hyphen (-).

The following attributes can be used for sorting: reports.swag_awarded_at, reports.bounty_awarded_at, reports.last_reporter_activity_at, reports.first_program_activity_at, reports.last_program_activity_at, reports.triaged_at, reports.created_at, reports.closed_at, reports.last_public_activity_at, reports.last_activity_at, and reports.disclosed_at.

Enumerated Values

| Parameter | Value |
| --- | --- |
| filter[state][] | new |
| filter[state][] | pending-program-review |
| filter[state][] | triaged |
| filter[state][] | needs-more-info |
| filter[state][] | resolved |
| filter[state][] | not-applicable |
| filter[state][] | informative |
| filter[state][] | duplicate |
| filter[state][] | spam |
| filter[state][] | retesting |
| filter[severity][] | none |
| filter[severity][] | low |
| filter[severity][] | medium |
| filter[severity][] | high |
| filter[severity][] | critical |

### Create Report

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "report",
    "attributes": {
      "team_handle": "string",
      "title": "string",
      "vulnerability_information": "string",
      "impact": "string",
      "severity_rating": "none",
      "weakness_id": 0,
      "structured_scope_id": 0,
      "source": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "report",
    "attributes": {
      "team_handle": "string",
      "title": "string",
      "vulnerability_information": "string",
      "impact": "string",
      "severity_rating": "none",
      "weakness_id": 0,
      "structured_scope_id": 0,
      "source": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "report",
    "attributes": {
      "team_handle": "string",
      "title": "string",
      "vulnerability_information": "string",
      "impact": "string",
      "severity_rating": "none",
      "weakness_id": 0,
      "structured_scope_id": 0,
      "source": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"report\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"title\": \"string\",\n      \"vulnerability_information\": \"string\",\n      \"impact\": \"string\",\n      \"severity_rating\": \"none\",\n      \"weakness_id\": 0,\n      \"structured_scope_id\": 0,\n      \"source\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"report\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"title\": \"string\",\n      \"vulnerability_information\": \"string\",\n      \"impact\": \"string\",\n      \"severity_rating\": \"none\",\n      \"weakness_id\": 0,\n      \"structured_scope_id\": 0,\n      \"source\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"report\",\n    \"attributes\": {\n      \"team_handle\": \"string\",\n      \"title\": \"string\",\n      \"vulnerability_information\": \"string\",\n      \"impact\": \"string\",\n      \"severity_rating\": \"none\",\n      \"weakness_id\": 0,\n      \"structured_scope_id\": 0,\n      \"source\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report created

```
{
  "id": "1337",
  "type": "report",
  "attributes": {
    "title": "XSS in login form",
    "state": "new",
    "created_at": "2016-02-02T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": null,
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "last_public_activity_at": null,
    "last_activity_at": null,
    "issue_tracker_reference_url": "https://example.com/reference",
    "cve_ids": [],
    "source": null,
    "reporter_agreed_on_going_public_at": null
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          },
          "reputation": 7,
          "signal": 7,
          "impact": 30
        }
      }
    },
    "collaborators": {
      "data": [
        {
          "weight": 1,
          "user": {
            "id": "1337",
            "type": "user",
            "attributes": {
              "username": "api-example",
              "name": "API Example",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        },
        {
          "weight": 1,
          "user": {
            "id": "1338",
            "type": "user",
            "attributes": {
              "username": "api-example 2",
              "name": "API Example 2",
              "disabled": false,
              "created_at": "2016-02-02T04:05:06.000Z",
              "profile_picture": {
                "62x62": "/assets/avatars/default.png",
                "82x82": "/assets/avatars/default.png",
                "110x110": "/assets/avatars/default.png",
                "260x260": "/assets/avatars/default.png"
              },
              "reputation": 7,
              "signal": 7,
              "impact": 30
            }
          }
        }
      ]
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "swag": {
      "data": []
    },
    "attachments": {
      "data": []
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "structured_scope": {
      "data": {
        "id": "287",
        "type": "structured-scope",
        "attributes": {
          "asset_type": "URL",
          "asset_identifier": "www.hackerone.com",
          "eligible_for_bounty": true,
          "eligible_for_submission": true,
          "instruction": "This asset does not contain any highly confidential information.",
          "max_severity": "critical",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z",
          "reference": "T12345",
          "confidentiality_requirement": "medium",
          "integrity_requirement": "high",
          "availability_requirement": "medium"
        }
      }
    },
    "campaign": null,
    "activities": {
      "data": []
    },
    "bounties": {
      "data": []
    },
    "summaries": {
      "data": []
    }
  }
}

```

Last revised: 2026-04-14

`POST /reports`

This API endpoint can be used to import known vulnerabilities into the HackerOne platform to detect duplicates and to encourage having a central vulnerability management system. When the API call is successful, a [report object](https://api.hackerone.com/customer-reference#report) will be returned.

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Note: If the program has required custom fields configured, reports created through this endpoint will return a 400 Bad Request error because custom field values cannot currently be provided via the API. To work around this, either remove the required constraint on custom fields in the program settings, or create the report through the HackerOne platform directly.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| data | body | object | true | The information to create a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» team_handle | body | string | true | The handle of the team that the report is being submitted to. |
| »» title | body | string | true | The title of the report. |
| »» vulnerability_information | body | string | true | Detailed information about the vulnerability including the steps to reproduce as well as supporting material and references. |
| »» impact | body | string | true | The security impact that an attacker could achieve. |
| »» severity_rating | body | [severity-ratings](https://api.hackerone.com/customer-reference#severity-ratings) | false | The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score. |
| »» weakness_id | body | integer | false | The ID of the weakness object that describes the type of the potential issue. |
| »» structured_scope_id | body | integer | false | The ID of the structured scope object that describes the attack surface. |
| »» source | body | string | true | A free-form string defining the source of the report for tracking purposes. For example, "detectify", "rapid7" or "jira". |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | report |
| »» severity_rating | none |
| »» severity_rating | low |
| »» severity_rating | medium |
| »» severity_rating | high |
| »» severity_rating | critical |

### Get Report

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/reports/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/reports/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/reports/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

report found

```
{
  "data": {
    "id": "1337",
    "type": "report",
    "attributes": {
      "title": "XSS in login form",
      "state": "new",
      "created_at": "2016-02-02T04:05:06.000Z",
      "vulnerability_information": "...",
      "triaged_at": null,
      "closed_at": null,
      "last_reporter_activity_at": null,
      "first_program_activity_at": null,
      "last_program_activity_at": null,
      "bounty_awarded_at": null,
      "swag_awarded_at": null,
      "disclosed_at": null,
      "source": null
    },
    "relationships": {
      "reporter": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "api-example",
            "name": "API Example",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "collaborators": {
        "data": [
          {
            "weight": 1,
            "user": {
              "id": "1337",
              "type": "user",
              "attributes": {
                "username": "api-example",
                "name": "API Example",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          },
          {
            "weight": 1,
            "user": {
              "id": "1338",
              "type": "user",
              "attributes": {
                "username": "api-example 2",
                "name": "API Example 2",
                "disabled": false,
                "created_at": "2016-02-02T04:05:06.000Z",
                "profile_picture": {
                  "62x62": "/assets/avatars/default.png",
                  "82x82": "/assets/avatars/default.png",
                  "110x110": "/assets/avatars/default.png",
                  "260x260": "/assets/avatars/default.png"
                },
                "reputation": 7,
                "signal": 7,
                "impact": 30
              }
            }
          }
        ]
      },
      "assignee": {
        "data": {
          "id": "1337",
          "type": "user",
          "attributes": {
            "username": "member",
            "name": "Member",
            "disabled": false,
            "created_at": "2016-02-02T04:05:06.000Z",
            "profile_picture": {
              "62x62": "/assets/avatars/default.png",
              "82x82": "/assets/avatars/default.png",
              "110x110": "/assets/avatars/default.png",
              "260x260": "/assets/avatars/default.png"
            }
          }
        }
      },
      "program": {
        "data": {
          "id": "1337",
          "type": "program",
          "attributes": {
            "handle": "security",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "severity": {
        "data": {
          "id": "57",
          "type": "severity",
          "attributes": {
            "rating": "high",
            "author_type": "User",
            "user_id": 1337,
            "created_at": "2016-02-02T04:05:06.000Z",
            "score": 8.7,
            "attack_complexity": "low",
            "attack_vector": "adjacent",
            "availability": "high",
            "confidentiality": "low",
            "integrity": "high",
            "privileges_required": "low",
            "user_interaction": "required",
            "scope": "changed"
          }
        }
      },
      "swag": {
        "data": []
      },
      "attachments": {
        "data": []
      },
      "weakness": {
        "data": {
          "id": "1337",
          "type": "weakness",
          "attributes": {
            "name": "Cross-Site Request Forgery (CSRF)",
            "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
            "external_id": "cwe-352",
            "created_at": "2016-02-02T04:05:06.000Z"
          }
        }
      },
      "structured_scope": {
        "data": {
          "id": "57",
          "type": "structured-scope",
          "attributes": {
            "asset_identifier": "api.example.com",
            "asset_type": "url",
            "confidentiality_requirement": "high",
            "integrity_requirement": "high",
            "availability_requirement": "high",
            "max_severity": "critical",
            "created_at": "2015-02-02T04:05:06.000Z",
            "updated_at": "2016-05-02T04:05:06.000Z",
            "instruction": null,
            "eligible_for_bounty": true,
            "eligible_for_submission": true,
            "reference": "H001001"
          }
        }
      },
      "campaign": null,
      "activities": {
        "data": [
          {
            "type": "activity-comment",
            "id": "445",
            "attributes": {
              "message": "Comment!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    },
                    "signal": null,
                    "impact": null,
                    "reputation": null,
                    "bio": null,
                    "website": null,
                    "location": null,
                    "hackerone_triager": false
                  }
                }
              },
              "attachments": {
                "data": [
                  {
                    "id": "1337",
                    "type": "attachment",
                    "attributes": {
                      "expiring_url": "/system/attachments/files/000/001/337/original/root.rb?1454385906",
                      "created_at": "2016-02-02T04:05:06.000Z",
                      "file_name": "root.rb",
                      "content_type": "text/x-ruby",
                      "file_size": 2871
                    }
                  }
                ]
              }
            }
          },
          {
            "id": "1337",
            "type": "activity-bug-resolved",
            "attributes": {
              "message": "Bug Resolved!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": false
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "1337",
                  "type": "user",
                  "attributes": {
                    "username": "api-example",
                    "name": "API Example",
                    "disabled": false,
                    "created_at": "2016-02-02T04:05:06.000Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    }
                  }
                }
              }
            }
          }
        ]
      },
      "bounties": {
        "data": []
      },
      "summaries": {
        "data": []
      },
      "inboxes": {
        "data": [
          {
            "id": "13",
            "type": "inbox",
            "attributes": {
              "name": "HackerOne",
              "type": "default"
            }
          },
          {
            "id": "65",
            "type": "inbox",
            "attributes": {
              "name": "Custom Inbox number one",
              "type": "custom"
            }
          }
        ]
      },
      "triggered_pre_submission_trigger": {
        "data": {
          "id": "1337",
          "type": "trigger",
          "attributes": {
            "title": "Example Trigger"
          }
        }
      },
      "custom_field_values": {
        "data": []
      },
      "automated_remediation_guidance": {
        "data": {
          "id": "1",
          "type": "automated-remediation-guidance",
          "attributes": {
            "reference": "https://cwe.mitre.org/data/definitions/120.html",
            "created_at": "2020-10-23T12:09:37.859Z"
          }
        }
      },
      "custom_remediation_guidance": {
        "data": {
          "id": "84",
          "type": "custom-remediation-guidance",
          "attributes": {
            "message": "Check buffer boundaries if accessing the buffer in a loop and make sure you are not in danger of writing past the allocated space.",
            "created_at": "2020-10-26T08:47:23.296Z"
          },
          "relationships": {
            "author": {
              "data": {
                "id": "1338",
                "type": "user",
                "attributes": {
                  "username": "api-example-2",
                  "name": "API Example 2",
                  "disabled": false,
                  "created_at": "2020-10-22T011:22:05.402Z",
                  "profile_picture": {
                    "62x62": "/assets/avatars/default.png",
                    "82x82": "/assets/avatars/default.png",
                    "110x110": "/assets/avatars/default.png",
                    "260x260": "/assets/avatars/default.png"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Last revised: 2026-04-14

`GET /reports/{id}`

A report object can be fetched by sending a GET request to a unique report object. In case the request was successful, the API will respond with a [report object](https://api.hackerone.com/customer-reference#report).

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |

### Update Reference

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id" \
  -X POST \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d @- <<EOD
{
  "data": {
    "type": "issue-tracker-reference-id",
    "attributes": {
      "reference": "string",
      "message": "string"
    }
  }
}
EOD

```

```
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

data = {
  "data": {
    "type": "issue-tracker-reference-id",
    "attributes": {
      "reference": "string",
      "message": "string"
    }
  }
}

r = requests.post(
  'https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  json = data,
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

data = {
  "data": {
    "type": "issue-tracker-reference-id",
    "attributes": {
      "reference": "string",
      "message": "string"
    }
  }
}

result = RestClient::Request.execute(
  method: :post,
  url: 'https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  payload: data,
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("POST");
con.setRequestProperty("Content-Type", "application/json; utf-8");
con.setRequestProperty("Accept", "application/json");
con.setDoOutput(true);
String jsonInputString = "{\n  \"data\": {\n    \"type\": \"issue-tracker-reference-id\",\n    \"attributes\": {\n      \"reference\": \"string\",\n      \"message\": \"string\"\n    }\n  }\n}";
try(OutputStream os = con.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
}

try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```
let inputBody = "{\n  \"data\": {\n    \"type\": \"issue-tracker-reference-id\",\n    \"attributes\": {\n      \"reference\": \"string\",\n      \"message\": \"string\"\n    }\n  }\n}";
let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "bytes"
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},

    }
    data := bytes.NewBuffer([]byte(`"{\n  \"data\": {\n    \"type\": \"issue-tracker-reference-id\",\n    \"attributes\": {\n      \"reference\": \"string\",\n      \"message\": \"string\"\n    }\n  }\n}"`))

    req, err := http.NewRequest("POST", "https://api.hackerone.com/v1/reports/{id}/issue_tracker_reference_id", data)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

reference updated

```
{
  "relationships": {
    "id": "77",
    "type": "report",
    "attributes": {
      "title": "XSS in login form",
      "state": "new",
      "created_at": "2019-08-20T14:26:19.286Z",
      "vulnerability_information": "...",
      "triaged_at": null,
      "closed_at": null,
      "last_reporter_activity_at": "2019-08-20T14:26:20.531Z",
      "first_program_activity_at": "2019-08-20T14:26:20.531Z",
      "last_program_activity_at": "2019-08-20T15:25:56.627Z",
      "bounty_awarded_at": null,
      "swag_awarded_at": null,
      "disclosed_at": null,
      "last_public_activity_at": "2019-08-20T15:25:56.627Z",
      "last_activity_at": "2019-08-20T15:25:56.627Z",
      "cve_ids": [],
      "source": null
    },
    "relationships": {
      "activities": {
        "data": [
          {
            "type": "activity-reference-id-added",
            "id": "<id>",
            "attributes": {
              "message": "Reference Id Added!",
              "created_at": "2016-02-02T04:05:06.000Z",
              "updated_at": "2016-02-02T04:05:06.000Z",
              "internal": true,
              "reference": "T7413",
              "reference_url": "https://example.com/T7413"
            },
            "relationships": {
              "actor": {
                "data": {
                  "id": "<id>",
                  "type": "user",
                  "attributes": {
                    "username": "api_user",
                    "name": null,
                    "disabled": false,
                    "created_at": "2019-10-14T13:59:49.563Z",
                    "profile_picture": {
                      "62x62": "/assets/avatars/default.png",
                      "82x82": "/assets/avatars/default.png",
                      "110x110": "/assets/avatars/default.png",
                      "260x260": "/assets/avatars/default.png"
                    },
                    "signal": null,
                    "impact": null,
                    "reputation": null,
                    "bio": null,
                    "website": null,
                    "location": null,
                    "hackerone_triager": false
                  }
                }
              }
            }
          }
        ]
      }
    }
  }
}

```

Last revised: 2026-04-14

`POST /reports/{id}/issue_tracker_reference_id`

This API allows the user to set a reference to an external issue tracker.

A report can only hold 1 active reference at the same time. However, a log of previously added references can be found in the activities relationship on a [report](https://api.hackerone.com/customer-reference#report) object. This API endpoint cannot be used for reports that have been reported outside of the HackerOne platform.

To begin setting up the integration with your issue tracker, check out the Integrations tab under your Program settings on [HackerOne.com](https://www.hackerone.com/).

Required permissions: Report Management. You can manage the permissions of your API users through your organization's settings. Insufficient permissions will result in a 403 Forbidden response.

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | integer | true | The ID of the report. |
| data | body | object | true | The information to update the reference of a report. |
| » type | body | string | true | none |
| » attributes | body | object | true | none |
| »» reference | body | string | true | The unique reference in the issue tracker. |
| »» message | body | string | false | The message that will be posted. |

Enumerated Values

| Parameter | Value |
| --- | --- |
| » type | issue-tracker-reference-id |

## Users

### Get User

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/users/{username}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/users/{username}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/users/{username}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/users/{username}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/users/{username}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/users/{username}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

user found

```
{
  "id": "1634",
  "username": "fransrosen",
  "name": "Frans Rosén",
  "reputation": 1337,
  "disabled": false,
  "signal": 7,
  "impact": 30,
  "created_at": "2015-13-37T04:05:06.000Z",
  "user_type": "hacker",
  "participating_programs": {
    "data": [
      {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2014-13-37T04:05:06.000Z",
          "updated_at": "2014-13-37T04:05:06.000Z"
        }
      }
    ]
  }
}

```

Last revised: 2025-05-23

`GET /users/{username}`

A user object can be fetched by providing the username of the given user. When the request is successful, the API will respond with a [user object](https://api.hackerone.com/customer-reference#user)

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | path | string | true | The HackerOne username of the user. |

### Get User By ID

Code samples

```
# You can also use wget
curl "https://api.hackerone.com/v1/user_by_id/{id}" \
  -X GET \
  -u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>" \
  -H 'Accept: application/json'

```

```
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get(
  'https://api.hackerone.com/v1/user_by_id/{id}',
  auth=('<YOUR_API_USERNAME>', '<YOUR_API_TOKEN>'),
  headers = headers
)

print(r.json())

```

```
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient::Request.execute(
  method: :get,
  url: 'https://api.hackerone.com/v1/user_by_id/{id}',
  password: '<YOUR_API_TOKEN>',
  user: '<YOUR_API_USERNAME>',
  headers: headers
)
p JSON.parse(result)

```

```
URL obj = new URL("https://api.hackerone.com/v1/user_by_id/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();

String userCredentials = "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>";
String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));
con.setRequestProperty ("Authorization", basicAuth);

con.setRequestMethod("GET");
try(BufferedReader br = new BufferedReader(
  new InputStreamReader(con.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
        response.append(responseLine.trim());
    }
    System.out.println(response.toString());
}

```

```

let user = '<YOUR_API_USERNAME>';
let password = '<YOUR_API_TOKEN>';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/user_by_id/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```
package main

import (
       "io/ioutil"
       "log"
       "net/http"
)

func main() { 
    headers := map[string][]string{
        "Accept": []string{"application/json"},

    }

    req, err := http.NewRequest("GET", "https://api.hackerone.com/v1/user_by_id/{id}", nil)
    req.Header = headers
    req.SetBasicAuth("<YOUR_API_USERNAME>", "<YOUR_API_TOKEN>")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)

    log.Println(string(body))
}

```

user found

```
{
  "id": "1634",
  "username": "fransrosen",
  "name": "Frans Rosén",
  "reputation": 1337,
  "disabled": false,
  "signal": 7,
  "impact": 30,
  "created_at": "2015-13-37T04:05:06.000Z",
  "user_type": "hacker",
  "participating_programs": {
    "data": [
      {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2014-13-37T04:05:06.000Z",
          "updated_at": "2014-13-37T04:05:06.000Z"
        }
      }
    ]
  }
}

```

Last revised: 2025-05-23

`GET /user_by_id/{id}`

A user object can be fetched by providing the id of the given user. When the request is successful, the API will respond with a [user object](https://api.hackerone.com/customer-reference#user)

Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | true | The HackerOne id of the user. |

Shell Python Ruby Java Javascript Go