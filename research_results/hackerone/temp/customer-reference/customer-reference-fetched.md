API Documentation NAV

# Customer Reference

The following section contains a complete reference of all the objects that can be returned through the API. Objects that have been explained earlier in this documentation are not included. The objects in this section are never top level resources by themselves and will only be returned as sub resources.

All objects are made up of an id and a type attribute. With those, additional attributes and relationships can be specified. An example how the data schema looks like, take a look at the response structure or the response object. Additional reading can be done at [jsonapi.org](http://jsonapi.org/).

## activity

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "report_id": "string",
    "message": "string",
    "internal": true,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
  "relationships": {
    "actor": {
      "data": {}
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

```

Last revised: 2024-02-08

These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program). Activities come in many sub types that can have additional attributes.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the activity. |
| type | string | true | Indicates what kind of activity it is. |
| attributes | object | true | none |
| » report_id | string | false | The report associated with the activity. |
| » message | string¦null | false | The comment associated with the activity. May be updated through theHackerOne interface. Markdown is not parsed. |
| » internal | boolean | true | Indicates if this activity can only be read by Program usersand external users that were invited to the report. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » actor | object | false | The author of the activity. |
| »» data | object | false | none |

oneOf - discriminator: user.type

Last revised: 2024-02-08

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| »»» anonymous | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

xor

Last revised: 2024-02-08

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| »»» anonymous | [program](https://api.hackerone.com/customer-reference#program) | false | A program object represents a disclosure program or bug bounty program on theplatform. When [a user](https://api.hackerone.com/customer-reference#user) reports a bug to a program, this isthe object they interact with. Behind a program, there can be multiple usersthat are part of the program. Those users can interact with reports on behalfof the program. |

continued

Last revised: 2024-02-08

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| » attachments | object | false | A list of Attachment objects added to the activity. |
| »» data | [[attachment](https://api.hackerone.com/customer-reference#attachment)] | false | [Users can add attachments when they file a report or when they interact with areport. Attachments may contain dangerous proof of concepts and should be handledwith caution.] |

### activity-agreed-on-going-public

```
{
  "id": "1337",
  "type": "activity-agreed-on-going-public",
  "attributes": {
    "report_id": "string",
    "message": "Agreed On Going Public!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-agreed-on-going-public | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» disclosed_at | string(date-time)¦null | false | none |
| »» allow_singular_disclosure_at | string(date-time)¦null | false | none |

### activity-bounty-awarded

```
{
  "id": "1337",
  "type": "activity-bounty-awarded",
  "attributes": {
    "report_id": "string",
    "message": "Bounty Awarded!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "bounty_amount": "500",
    "bonus_amount": "50"
  },
  "relationships": {
    "actor": {
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bounty-awarded | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» bounty_amount | string | false | none |
| »» bonus_amount | string | false | none |

### activity-bounty-suggested

```
{
  "id": "1337",
  "type": "activity-bounty-suggested",
  "attributes": {
    "report_id": "string",
    "message": "Bounty Suggested!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bounty-suggested | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» bounty_amount | string | false | none |
| »» bonus_amount | string | false | none |

### activity-bug-cloned

```
{
  "id": "1337",
  "type": "activity-bug-cloned",
  "attributes": {
    "report_id": "string",
    "message": "Bug Cloned!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "original_report_id": 1336
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-cloned | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» original_report_id | integer | true | none |

### activity-bug-duplicate

```
{
  "id": "1337",
  "type": "activity-bug-duplicate",
  "attributes": {
    "report_id": "string",
    "message": "Bug Duplicate!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "original_report_id": 1336
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-duplicate | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» original_report_id | integer | false | none |

### activity-bug-filed

```
{
  "id": "7331",
  "type": "activity-bug-filed",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "actor": {
      "data": {
        "type": "user",
        "id": "1337",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2017-11-09T10:52:25.443Z",
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-filed | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-inactive

```
{
  "id": "1337",
  "type": "activity-bug-inactive",
  "attributes": {
    "report_id": "string",
    "message": "Bug closed automatically due to inactivity in the last 30 days.",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "actor": {
      "data": null
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-inactive | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-informative

```
{
  "id": "1337",
  "type": "activity-bug-informative",
  "attributes": {
    "report_id": "string",
    "message": "Bug Informative!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-informative | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-needs-more-info

```
{
  "id": "1337",
  "type": "activity-bug-needs-more-info",
  "attributes": {
    "report_id": "string",
    "message": "Bug Needs More Info!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-needs-more-info | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-new

```
{
  "id": "1337",
  "type": "activity-bug-new",
  "attributes": {
    "report_id": "string",
    "message": "Bug New!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-new | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-not-applicable

```
{
  "id": "1337",
  "type": "activity-bug-not-applicable",
  "attributes": {
    "report_id": "string",
    "message": "Bug Not Applicable!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-not-applicable | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-priority-changed

```
{
  "id": "1337",
  "type": "activity-bug-priority-changed",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "priority": "high"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-priority-changed | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» priority | string¦null | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| priority | high |
| priority | regular |

### activity-bug-reopened

```
{
  "id": "1337",
  "type": "activity-bug-reopened",
  "attributes": {
    "report_id": "string",
    "message": "Bug Reopened!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-reopened | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-resolved

```
{
  "id": "1337",
  "type": "activity-bug-resolved",
  "attributes": {
    "report_id": "string",
    "message": "Bug Resolved!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-resolved | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-retesting

```
{
  "id": "1337",
  "type": "activity-bug-retesting",
  "attributes": {
    "report_id": "string",
    "message": "Please retest this report.",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-retesting | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-spam

```
{
  "id": "1337",
  "type": "activity-bug-spam",
  "attributes": {
    "report_id": "string",
    "message": "Bug Spam!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-spam | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-bug-triaged

```
{
  "id": "1337",
  "type": "activity-bug-triaged",
  "attributes": {
    "report_id": "string",
    "message": "Bug Triaged!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-bug-triaged | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-cancelled-disclosure-request

```
{
  "id": "1337",
  "type": "activity-cancelled-disclosure-request",
  "attributes": {
    "report_id": "string",
    "message": "Cancel disclosure 1",
    "internal": false,
    "created_at": "2019-10-23T13:35:35.616Z",
    "updated_at": "2019-10-23T13:35:35.616Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-cancelled-disclosure-request | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-changed-scope

```
{
  "id": "1337",
  "type": "activity-changed-scope",
  "attributes": {
    "report_id": "string",
    "message": "A different scope has added",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "old_scope": {
      "data": {
        "id": "1337",
        "type": "structured_scope",
        "attributes": {
          "asset_identifier": "www.example.com",
          "asset_type": "url",
          "confidentiality_requirement": null,
          "integrity_requirement": null,
          "availability_requirement": null,
          "max_severity": "critical",
          "created_at": "2015-02-02T04:05:06.000Z",
          "updated_at": "2016-05-02T04:05:06.000Z",
          "instruction": "not eligible for bounty",
          "eligible_for_bounty": false,
          "eligible_for_submission": true
        }
      }
    },
    "new_scope": {
      "data": {
        "id": "1338",
        "type": "structured_scope",
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
          "eligible_for_submission": true
        }
      }
    }
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-changed-scope | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» old_scope | object | true | none |
| »»» data | [structured-scope](https://api.hackerone.com/customer-reference#structured-scope) | false | A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program. |
| »» new_scope | object | true | none |
| »»» data | [structured-scope](https://api.hackerone.com/customer-reference#structured-scope) | false | A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program. |

### activity-comment

```
{
  "id": "1337",
  "type": "activity-comment",
  "attributes": {
    "report_id": "string",
    "message": "Comment!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-comment | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-comments-closed

```
{
  "id": "1337",
  "type": "activity-comments-closed",
  "attributes": {
    "report_id": "string",
    "message": "Comments Closed!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-comments-closed | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-draft-started

```
{
  "id": "1337",
  "type": "activity-draft-started",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-draft-started | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-external-user-invitation-cancelled

```
{
  "id": "1337",
  "type": "activity-external-user-invitation-cancelled",
  "attributes": {
    "report_id": "string",
    "message": "External User Invitation Cancelled!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "email": "hacker@example.com"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-external-user-invitation-cancelled | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» email | string¦null | false | none |

### activity-external-user-invited

```
{
  "id": "1337",
  "type": "activity-external-user-invited",
  "attributes": {
    "report_id": "string",
    "message": "External User Invited!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "email": "hacker@example.com"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-external-user-invited | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» email | string¦null | false | none |

### activity-external-user-joined

```
{
  "id": "1337",
  "type": "activity-external-user-joined",
  "attributes": {
    "report_id": "string",
    "message": "External User Joined!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "duplicate_report_id": 10
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-external-user-joined | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» duplicate_report_id | integer | false | none |

### activity-external-user-removed

```
{
  "id": "1337",
  "type": "activity-external-user-removed",
  "attributes": {
    "report_id": "string",
    "message": "External User Removed!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "removed_user": {
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

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-external-user-removed | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» removed_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

### activity-group-assigned-to-bug

```
{
  "id": "1337",
  "type": "activity-group-assigned-to-bug",
  "attributes": {
    "report_id": "string",
    "message": "Group Assigned To Bug!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "group": {
      "data": {
        "id": "1337",
        "type": "group",
        "attributes": {
          "name": "Admin",
          "created_at": "2016-02-02T04:05:06.000Z",
          "permissions": [
            "user_management",
            "report_management"
          ]
        }
      }
    }
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-group-assigned-to-bug | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» group | object | true | none |
| »»» data | [group](https://api.hackerone.com/customer-reference#group) | false | A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports. |

### activity-hacker-requested-mediation

```
{
  "id": "1337",
  "type": "activity-hacker-requested-mediation",
  "attributes": {
    "report_id": "string",
    "message": "Hacker Requested Mediation!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-hacker-requested-mediation | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-invitation-received

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "report_id": "string",
    "message": "string",
    "internal": true,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
  "relationships": {
    "actor": {
      "data": {}
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
  },
  "data": {
    "type": "activity-invitation-received",
    "id": "1337",
    "attributes": {
      "message": "Activity Invitation Received",
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
            "username": "hacker",
            "name": "Hacker",
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
            "bio": "Super great hacker",
            "website": "http://hackerone.com",
            "location": "Who wants to know?",
            "hackerone_triager": false
          }
        }
      }
    }
  }
}

```

Last revised: 2023-07-06

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-invitation-received | any | false | none |

allOf

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-manually-disclosed

```
{
  "id": "1337",
  "type": "activity-manually-disclosed",
  "attributes": {
    "report_id": "string",
    "message": "Manually Disclosed!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-manually-disclosed | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-mediation-requested

```
{
  "id": "1337",
  "type": "activity-mediation-requested",
  "attributes": {
    "report_id": "string",
    "message": "Mediation Requested!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-mediation-requested | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-nobody-assigned-to-bug

```
{
  "id": "1337",
  "type": "activity-nobody-assigned-to-bug",
  "attributes": {
    "report_id": "string",
    "message": "Nobody Assigned To Bug!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-nobody-assigned-to-bug | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-not-eligible-for-bounty

```
{
  "id": "1337",
  "type": "activity-not-eligible-for-bounty",
  "attributes": {
    "report_id": "string",
    "message": "Not Eligible For Bounty!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-not-eligible-for-bounty | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-program-hacker-joined

```
{
  "id": "1337",
  "type": "activity-program-hacker-joined",
  "attributes": {
    "report_id": "string",
    "message": "Program hacker joined",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "actor": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "new_hacker",
          "name": "NEW HACKER",
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
          "bio": "Super great hacker",
          "website": "http://hackerone.com",
          "location": "Who wants to know?",
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
    },
    "program": {
      "id": "1337",
      "type": "program",
      "attributes": {
        "handle": "team_shine",
        "policy": "Policy definition",
        "created_at": "2016-02-02T04:05:06.000Z",
        "updated_at": "2016-02-02T04:05:06.000Z"
      }
    }
  }
}

```

Last revised: 2023-07-06

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-program-hacker-joined | any | false | none |

allOf

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-program-hacker-left

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "report_id": "string",
    "message": "string",
    "internal": true,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
  "relationships": {
    "actor": {
      "data": {}
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
  },
  "data": {
    "activity": {
      "type": "activity-program-hacker-left",
      "id": "1337",
      "attributes": {
        "message": "Message",
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
              "username": "leaving_hacker",
              "name": "LEAVING HACKER",
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
              "bio": "Super great hacker",
              "website": "http://hackerone.com",
              "location": "Who wants to know?",
              "hackerone_triager": false
            }
          }
        },
        "program": {
          "id": "1337",
          "type": "program",
          "attributes": {
            "handle": "team_shine",
            "policy": "Policy definition",
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z"
          }
        }
      }
    }
  }
}

```

Last revised: 2023-07-06

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-program-hacker-left | any | false | none |

allOf

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2023-07-06

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-program-inactive

```
{
  "id": "1337",
  "type": "activity-program-inactive",
  "attributes": {
    "report_id": "string",
    "message": "Closed report and changed status to Informative due to inactive state of program.",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "actor": {
      "data": null
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-program-inactive | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-reassigned-to-team

```
{
  "id": "1337",
  "type": "activity-reassigned-to-team",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-reassigned-to-team | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-recommendation-created

```
{
  "id": "1337",
  "type": "activity-recommendation-created",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "recommended_action": "close_as_duplicate"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-recommendation-created | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» recommended_action | string¦null | false | none |

### activity-reference-id-added

```
{
  "id": "1337",
  "type": "activity-reference-id-added",
  "attributes": {
    "report_id": "string",
    "message": "Reference Id Added!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "reference": "reference",
    "reference_url": "https://example.com/reference"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-reference-id-added | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» reference | string | true | none |
| »» reference_url | string | true | none |

### activity-report-became-public

```
{
  "id": "1337",
  "type": "activity-report-became-public",
  "attributes": {
    "report_id": "string",
    "message": "Report Became Public!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
  },
  "relationships": {
    "actor": {
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-became-public | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-collaborator-invited

```
{
  "id": "1337",
  "type": "activity-report-collaborator-invited",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "email": "h...r@example.com"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-collaborator-invited | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» email | string¦null | false | none |

### activity-report-collaborator-joined

```
{
  "id": "1337",
  "type": "activity-report-collaborator-joined",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-collaborator-joined | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-custom-field-value-updated

```
{
  "id": "1337",
  "type": "activity-report-custom-field-value-updated",
  "attributes": {
    "report_id": "string",
    "message": "Custom Field Value Updated!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "old_value": "Infra",
    "new_value": "Infrastructure"
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
    },
    "custom_field_attribute": {
      "data": {
        "id": "287",
        "type": "custom-field-attribute",
        "attributes": {
          "label": "Product Squad",
          "configuration": null,
          "created_at": "2013-01-01T00:00:00.000Z",
          "updated_at": "2013-01-01T00:00:00.000Z",
          "archived_at": null
        }
      }
    }
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-custom-field-value-updated | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-prioritised

```
{
  "id": "1337",
  "type": "activity-report-prioritised",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "high_priority": true,
    "high_priority_reason": null
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

```

Last revised: 2026-01-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-prioritised | any | false | none |

allOf

Last revised: 2026-01-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-01-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» high_priority | boolean | true | none |
| »» high_priority_reason | string¦null | false | none |

### activity-report-remediation-guidance-updated

```
{
  "id": "1337",
  "type": "activity-report-remediation-guidance-updated",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-remediation-guidance-updated | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-retest-approved

```
{
  "id": "1337",
  "type": "activity-report-retest-approved",
  "attributes": {
    "report_id": "string",
    "message": "The retest results look good!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-retest-approved | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-retest-rejected

```
{
  "id": "1337",
  "type": "activity-report-retest-rejected",
  "attributes": {
    "report_id": "string",
    "message": "Please provide more context for the retest next time.",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-retest-rejected | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-severity-updated

```
{
  "id": "1337",
  "type": "activity-report-severity-updated",
  "attributes": {
    "report_id": "string",
    "message": "Report Severity Updated!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "old_severity": {
      "data": {
        "id": "1337",
        "type": "severity",
        "attributes": {
          "rating": "high",
          "author_type": "User",
          "user_id": "56",
          "created_at": "2016-02-02T04:05:06.000Z",
          "score": 8.7,
          "attack_complexity": "low",
          "attack_vector": "adjacent",
          "confidentiality": "low",
          "integrity": "high",
          "availability": "high",
          "privileges_required": "low",
          "user_interaction": "required",
          "scope": "changed",
          "confidentiality_requirement": "not_defined",
          "integrity_requirement": "not_defined",
          "availability_requirement": "not_defined",
          "max_severity": "none",
          "calculation_method": "cvss_3_0_hackerone"
        }
      }
    },
    "new_severity": {
      "data": {
        "id": "1337",
        "type": "severity",
        "attributes": {
          "rating": "medium",
          "author_type": "Team",
          "user_id": "56",
          "created_at": "2016-02-02T04:05:06.000Z",
          "score": 5.2,
          "attack_complexity": "low",
          "attack_vector": "physical",
          "confidentiality": "high",
          "integrity": "none",
          "availability": "low",
          "privileges_required": "none",
          "user_interaction": "none",
          "scope": "unchanged",
          "confidentiality_requirement": "not_defined",
          "integrity_requirement": "not_defined",
          "availability_requirement": "not_defined",
          "max_severity": "none",
          "calculation_method": "cvss_3_0_hackerone"
        }
      }
    }
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-severity-updated | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-title-updated

```
{
  "id": "1337",
  "type": "activity-report-title-updated",
  "attributes": {
    "report_id": "string",
    "message": "Report Title Updated!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "old_title": "xss",
    "new_title": "XSS in login form"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-title-updated | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» old_title | string | true | none |
| »» new_title | string | true | none |

### activity-report-triage-summary-created

```
{
  "id": "1337",
  "type": "activity-report-triage-summary-created",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-03-11

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-triage-summary-created | any | false | none |

allOf

Last revised: 2026-03-11

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-03-11

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-triage-summary-updated

```
{
  "id": "1337",
  "type": "activity-report-triage-summary-updated",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-03-13

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-triage-summary-updated | any | false | none |

allOf

Last revised: 2026-03-13

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-03-13

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-vulnerability-information-updated

```
{
  "id": "1337",
  "type": "activity-report-vulnerability-information-updated",
  "attributes": {
    "report_id": "string",
    "message": "string",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2024-05-23

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-vulnerability-information-updated | any | false | none |

allOf

Last revised: 2024-05-23

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2024-05-23

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-report-vulnerability-types-updated

```
{
  "id": "1337",
  "type": "activity-report-vulnerability-types-updated",
  "attributes": {
    "report_id": "string",
    "message": "Report Vulnerability Types Updated!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "old_weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cryptographic Issues - Generic",
          "description": "Weaknesses in this category are related to the use of cryptography.",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "new_weakness": {
      "data": {
        "id": "1338",
        "type": "weakness",
        "attributes": {
          "name": "Use of Hard-coded Cryptographic Key",
          "description": "The use of a hard-coded cryptographic key significantly increases the possibility that encrypted data may be recovered.",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    }
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-report-vulnerability-types-updated | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» old_weakness | object | false | The weakness that was set before the change |
| »»» data | [weakness](https://api.hackerone.com/customer-reference#weakness) | false | A Weakness object represents the type of weakness the hacker submitted to a program.The weakness was initially provided by the hacker, but may be reviewed and correctedby the program. |
| »» new_weakness | object | false | The weakness that was set after the change |
| »»» data | [weakness](https://api.hackerone.com/customer-reference#weakness) | false | A Weakness object represents the type of weakness the hacker submitted to a program.The weakness was initially provided by the hacker, but may be reviewed and correctedby the program. |

### activity-retest-user-expired

```
{
  "id": "1337",
  "type": "activity-retest-user-expired",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-retest-user-expired | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-swag-awarded

```
{
  "id": "1337",
  "type": "activity-swag-awarded",
  "attributes": {
    "report_id": "string",
    "message": "Swag Awarded!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "swag": {
      "data": {
        "id": "1337",
        "type": "swag",
        "attributes": {
          "sent": false,
          "created_at": "2016-02-02T04:05:06.000Z"
        },
        "relationships": {
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
  }
}

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-swag-awarded | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» swag | object | true | none |
| »»» data | [swag](https://api.hackerone.com/customer-reference#swag) | false | Besides a financial reward, which is called [a bounty](https://api.hackerone.com/customer-reference#bounty), programs canaward swag. Report objects may contain multiple swag objects, one for each timeswag was awarded. |

### activity-triage-intake-completed

```
{
  "id": "1337",
  "type": "activity-triage-intake-completed",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "high_priority": "true"
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

```

Last revised: 2025-05-27

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-triage-intake-completed | any | false | none |

allOf

Last revised: 2025-05-27

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2025-05-27

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» reference | string | false | none |
| »» reference_url | string | false | none |

### activity-triage-intake-exited

```
{
  "id": "1337",
  "type": "activity-triage-intake-exited",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "intake_outcome": "closed",
    "abort_reason": "analyst_end_intake",
    "va_suggestion": null,
    "report_state_change": "spam"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-triage-intake-exited | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | false | none |
| »» intake_outcome | string¦null | false | none |
| »» abort_reason | string¦null | false | none |
| »» va_suggestion | string¦null | false | none |
| »» report_state_change | string¦null | false | none |

### activity-user-assigned-to-bug

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "report_id": "string",
    "message": "string",
    "internal": true,
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
  "relationships": {
    "actor": {
      "data": {}
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
  },
  "data": {
    "id": "1337",
    "type": "activity-user-assigned-to-bug",
    "attributes": {
      "message": "User Assigned To Bug!",
      "created_at": "2016-02-02T04:05:06.000Z",
      "updated_at": "2016-02-02T04:05:06.000Z",
      "internal": true
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
      "assigned_user": {
        "data": {
          "id": "1336",
          "type": "user",
          "attributes": {
            "username": "other_user",
            "name": "Other User",
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

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-user-assigned-to-bug | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» assigned_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

### activity-user-banned-from-program

```
{
  "id": "1337",
  "type": "activity-user-banned-from-program",
  "attributes": {
    "report_id": "string",
    "message": "User Banned From Program!",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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
    },
    "removed_user": {
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

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-user-banned-from-program | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » relationships | object | false | none |
| »» removed_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

### activity-user-completed-retest

```
{
  "id": "1337",
  "type": "activity-user-completed-retest",
  "attributes": {
    "report_id": "string",
    "message": "User Completed Retest!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-user-completed-retest | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-user-left-retest

```
{
  "id": "1337",
  "type": "activity-user-left-retest",
  "attributes": {
    "report_id": "string",
    "message": "User left Retest!",
    "internal": false,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-user-left-retest | any | false | none |

allOf

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2021-06-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-validation-recommendation-accepted

```
{
  "id": "1337",
  "type": "activity-validation-recommendation-accepted",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-validation-recommendation-accepted | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

### activity-validation-recommendation-rejected

```
{
  "id": "1337",
  "type": "activity-validation-recommendation-rejected",
  "attributes": {
    "report_id": "string",
    "message": "",
    "internal": true,
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z"
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

```

Last revised: 2026-04-30

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| activity-validation-recommendation-rejected | any | false | none |

allOf

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [activity](https://api.hackerone.com/customer-reference#activity) | false | These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes. |

and

Last revised: 2026-04-30

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |

## address

```
{
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

```

Last revised: 2023-09-14

This object contains the postal address for the delivery of awarded [swag](https://api.hackerone.com/customer-reference#swag).

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the address. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | none |
| » street | string | true | none |
| » city | string | true | none |
| » postal_code | string | true | none |
| » state | string | true | none |
| » country | string | true | none |
| » tshirt_size | string | false | none |
| » phone_number | string | false | none |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | address |
| tshirt_size | M_Small |
| tshirt_size | M_Medium |
| tshirt_size | M_Large |
| tshirt_size | M_XLarge |
| tshirt_size | M_XXLarge |
| tshirt_size | W_Small |
| tshirt_size | W_Medium |
| tshirt_size | W_Large |
| tshirt_size | W_XLarge |
| tshirt_size | W_XXLarge |

## allowed_reporter

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

Last revised: 2025-06-10

Allowed reporter objects represent researchers that belong to a private program on HackerOne. These are users that engage with your program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the user. This is the same ID as in the [user objects](https://api.hackerone.com/customer-reference#allowed_reporter). |
| type | string | true | none |
| attributes | object | true | none |
| » username | string | true | The username of the allowed reporter. |
| » email_alias | string | true | The HackerOne provided email for direct communication (@wearehackerone.com domain). |
| » rules_of_engagement_signed | boolean | false | Whether the user has signed the [clear rules of engagement](https://www.hackerone.com/policies/clear-rules-of-engagement). |
| » identity_verified | boolean | true | Whether the user has [verified their identity](https://docs.hackerone.com/en/articles/8399430-id-verification) with HackerOne. |
| » background_checked | boolean | true | Whether the user has [passed a background check](https://docs.hackerone.com/en/articles/8404292-background-checks). |
| » cleared | boolean | true | Whether the user is currently [cleared](https://docs.hackerone.com/organizations/hackerone-clear.html). |
| » citizenship_verified | boolean | true | Whether the user has [verified](https://docs.hackerone.com/en/articles/8688126-residency-citizenship-checks) at least one citizenship with HackerOne. |
| » residency_verified | boolean | true | Whether the user has [verified](https://docs.hackerone.com/en/articles/8688126-residency-citizenship-checks) at least one residency with HackerOne. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | allowed_reporter |

## allowed-reporter-history-entry

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

Last revised: 2025-03-25

Allowed reporter history entry objects represent the history of a user's involvement in a private program as an allowed reporter.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the allowed reporter history entry. |
| type | string | true | none |
| attributes | object | true | none |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |
| » invited_at | string(date-time) | false | The date and time the user was invited to join the private program.Formatted according to ISO 8601. |
| relationships | object | true | none |
| » user | object | true | The user object associated with the allowed reporter history entry. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | allowed-reporter-history-entry |

## allowed_reporter_username_history

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

Last revised: 2023-11-21

Allowed Reporter Username History contains the old usernames of an [allowed reporter](https://api.hackerone.com/customer-reference#allowed_reporter).

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| attributes | object | true | none |
| » user_id | string | true | The unique id of the allowed reporter. |
| » old_usernames | [string] | true | Old usernames of the allowed reporter (deprecated). |

## analytics

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

Last revised: 2022-11-10

Analytics queries are predefined GraphQL queries to retrieve commonly used metrics

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| keys | array | false | The field names for the queried data |
| values | array | false | The values for the queried data |

## attachment

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

Last revised: 2025-06-10

Users can add attachments when they file a report or when they interact with a report. Attachments may contain dangerous proof of concepts and should be handled with caution.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the attachment. |
| type | string | true | none |
| attributes | object | true | none |
| » file_name | string | true | The file name of the attachment. |
| » content_type | string | true | The content type of the attachment. The content type is derived from thecontents and extension of the file. |
| » file_size | integer | true | The file size of the attachment in bytes. |
| » expiring_url | string | true | A URL to download the attachment. The URL will automatically expire after60 minutes. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | attachment |

## audit-log

```
{
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

```

Last revised: 2025-03-25

An audit log item contains information to determine who did what in an organization or program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the audit log item. |
| type | string | true | Indicates what kind of object it is. |
| attributes | object | true | none |
| » log | string | true | A human-readable log entry describing what happened. |
| » event | [audit-log-events](https://api.hackerone.com/customer-reference#audit-log-events) | true | The event that created the audit log item. |
| » source | string | true | A unique identifier that indicates the source of the audit log item. |
| » subject | string | true | A unique identifier that indicates the subject of the audit log item. |
| » user_agent | string¦null | false | An optional string that contains the user agent specified by the client. |
| » country | string¦null | false | An optional ISO 3166 country code. XX means that the countrycouldn't be found. T1 is a Tor node. |
| » parameters | string | true | A serialized JSON object containing the data that was used to constructthe audit log. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |
| relationships | object | false | none |
| » source_user | object¦null | false | The user who triggered the event. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

## audit-log-events

```
"teams.agile_accelerator_integration.delete"

```

Last revised: 2025-03-25

The event that created the audit log item.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| audit-log-events | string | false | The event that created the audit log item. |

Enumerated Values

| Property | Value |
| --- | --- |
| audit-log-events | teams.agile_accelerator_integration.delete |
| audit-log-events | teams.agile_accelerator_integration.update |
| audit-log-events | teams.api_users.create |
| audit-log-events | teams.api_users.destroy |
| audit-log-events | teams.audit_log_items.export |
| audit-log-events | teams.blocklisted.hacker.block |
| audit-log-events | teams.blocklisted.hacker.unblock |
| audit-log-events | teams.bounties.create |
| audit-log-events | teams.bounties.schedule |
| audit-log-events | teams.clickthrough_agreement.update |
| audit-log-events | teams.consumption_tier_override.create_or_update |
| audit-log-events | teams.consumption_tier_override.delete |
| audit-log-events | teams.gateway_cloudflared_tunnel.create |
| audit-log-events | teams.gateway_cloudflared_tunnel.delete |
| audit-log-events | teams.gateway_compliance_log_request.create |
| audit-log-events | teams.gateway_program_vpn_state.update |
| audit-log-events | teams.gateway_program_ipsec_settings.update |
| audit-log-events | teams.gateway_program_gateway_scopes.update |
| audit-log-events | teams.gateway_users_vpn_state.update |
| audit-log-events | teams.clearance.update |
| audit-log-events | teams.groups.create |
| audit-log-events | teams.groups.update |
| audit-log-events | teams.groups.destroy |
| audit-log-events | teams.invitations.members.create |
| audit-log-events | teams.invitations.report_participants.create |
| audit-log-events | teams.jira_integration.create |
| audit-log-events | teams.jira_integration.update |
| audit-log-events | teams.jira_integration.verify |
| audit-log-events | teams.jira_integration.destroy |
| audit-log-events | teams.members.destroy |
| audit-log-events | teams.member_eligibility.update |
| audit-log-events | teams.reports.escalate |
| audit-log-events | teams.reports.reference.destroy |
| audit-log-events | teams.report.reassign |
| audit-log-events | teams.reports.export |
| audit-log-events | teams.reports.export_lifetime |
| audit-log-events | teams.reports.exports.pentest |
| audit-log-events | teams.reports.retest.approve |
| audit-log-events | teams.saml_settings.update |
| audit-log-events | teams.slack_integration.create |
| audit-log-events | teams.slack_integration.destroy |
| audit-log-events | teams.slack_pipeline.create |
| audit-log-events | teams.slack_pipeline.update |
| audit-log-events | teams.slack_pipeline.destroy |
| audit-log-events | teams.webhook.delete |
| audit-log-events | teams.update |
| audit-log-events | teams.webhook.create |
| audit-log-events | teams.webhook.update |
| audit-log-events | teams.webhook.destroy |
| audit-log-events | teams.webhook.test_request |
| audit-log-events | teams.allowlisted.hacker.add |
| audit-log-events | teams.allowlisted.hacker.removed.quit |
| audit-log-events | teams.allowlisted.hacker.removed |
| audit-log-events | teams.tray.solution_instance.create |
| audit-log-events | teams.tray.solution_instance.update |
| audit-log-events | teams.tray.solution_instance.destroy |
| audit-log-events | teams.tray.solution_instance.test |
| audit-log-events | teams.tray.destroy_integration |
| audit-log-events | teams.common_response.create |
| audit-log-events | teams.common_response.update |
| audit-log-events | teams.common_response.destroy |
| audit-log-events | teams.organization.change |
| audit-log-events | organizations.update |
| audit-log-events | organizations.audit_log_items.export |
| audit-log-events | organizations.tray.solution_instance.update |
| audit-log-events | organizations.tray.destroy_integration |
| audit-log-events | organizations.members.create |
| audit-log-events | organizations.members.destroy |
| audit-log-events | organizations.members.update |
| audit-log-events | organizations.members.toggle_admin |
| audit-log-events | organizations.api_token.create |
| audit-log-events | organizations.api_token.destroy |
| audit-log-events | organizations.scim_user.create |
| audit-log-events | organizations.scim_user.refresh |
| audit-log-events | organizations.domain_ownerships.cancel |
| audit-log-events | organizations.domain_ownerships.create |
| audit-log-events | organizations.domain_ownerships.verify |
| audit-log-events | organizations.eligibility_settings.update |
| audit-log-events | organizations.eligibility_settings.destroy |
| audit-log-events | organizations.eligibility_settings.create |
| audit-log-events | organizations.saml_providers.create |
| audit-log-events | organizations.saml_providers.update_testing |
| audit-log-events | organizations.saml_providers.update_locked |
| audit-log-events | organizations.saml_providers.verify |
| audit-log-events | organizations.saml_providers.enable |
| audit-log-events | organizations.saml_providers.delete |
| audit-log-events | organizations.saml_providers.disable |
| audit-log-events | organizations.saml_providers.reject |
| audit-log-events | organizations.saml_providers.migrate_users |
| audit-log-events | organizations.saml_providers.add_provisioning_config |
| audit-log-events | organizations.saml_providers.update_alternative_certificate |
| audit-log-events | organizations.saml_providers.swapped_certificates |
| audit-log-events | organizations.saml_providers.certificates_replaced |
| audit-log-events | organizations.member_groups.create |
| audit-log-events | organizations.member_groups.destroy |
| audit-log-events | organizations.member_groups.update |
| audit-log-events | organizations.automations.create |
| audit-log-events | organizations.automations.update |
| audit-log-events | organizations.automations.update_enabled |
| audit-log-events | organizations.automations.update_archived |
| audit-log-events | organizations.automations.invoke |
| audit-log-events | organizations.workboards.create |
| audit-log-events | organizations.workboards.update |
| audit-log-events | organizations.workboards.delete |
| audit-log-events | organizations.workboards.provision |
| audit-log-events | organizations.workboard_views.create |
| audit-log-events | organization.workboard_views.delete |
| audit-log-events | organization.workboard_views.rename |
| audit-log-events | organization.workboard_views.update |
| audit-log-events | organizations.inboxes.create |
| audit-log-events | organizations.inboxes.destroy |
| audit-log-events | organizations.inboxes.update |
| audit-log-events | organizations.reports.export |
| audit-log-events | organizations.invitations.members.create |
| audit-log-events | organizations.invitations.members.cancel |
| audit-log-events | organizations.asset.create |
| audit-log-events | organizations.assets.export |
| audit-log-events | organizations.analytics_report.create |
| audit-log-events | organizations.analytics_report.delete |
| audit-log-events | organizations.analytics_report.rename |
| audit-log-events | organizations.analytics_report.download |
| audit-log-events | organizations.hai.toggled |
| audit-log-events | organizations.automations.user_created |
| audit-log-events | reports.vulnerability_information.read |

## automated-remediation-guidance

```
{
  "data": {
    "id": "1",
    "type": "automated-remediation-guidance",
    "attributes": {
      "reference": "https://cwe.mitre.org/data/definitions/120.html",
      "created_at": "2020-10-23T12:09:37.859Z"
    }
  }
}

```

Last revised: 2021-06-25

Remediation guidance that has been derived from the report's weakness.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the automated remediation guidance. |
| type | string | true | Indicates what kind of object it is. |
| attributes | object | true | none |
| » reference | string | true | The URL of the remediation guidance article. |
| » created_at | string(date-time) | true | The date and time the automated remediation guidance was created.Formatted according to ISO 8601. |

## bounty

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

Last revised: 2023-04-27

When a program pays a bounty to the hacker, a bounty object is created. A report may contain multiple bounty objects, one for each time a bounty was awarded. The hacker that reported the vulnerability is the user that received the bounty.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the bounty. |
| type | string | true | none |
| attributes | object | true | none |
| » amount | string¦null | false | Amount in USD. |
| » bonus_amount | string¦null | false | Bonus amount in USD. |
| » awarded_amount | string¦null | false | Amount in awarded currency. |
| » awarded_bonus_amount | string¦null | false | Bonus amount in awarded currency. |
| » awarded_currency | string¦null | false | The currency used to award the bounty and bonus. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | bounty |

## campaign

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

A campaign object represents a bounty campaign for a program. Campaigns allow program managers to incentivize hackers by offering bounty multipliers on specific assets for a limited time.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the campaign. |
| type | string | true | none |
| attributes | object | true | none |
| » campaign_type | string | true | The type of campaign (e.g. "multiplier"). |
| » researchers_information | string¦null | false | Additional information for researchers about the campaign. |
| » critical | number(float)¦null | false | The bounty multiplier for critical severity findings. |
| » high | number(float)¦null | false | The bounty multiplier for high severity findings. |
| » medium | number(float)¦null | false | The bounty multiplier for medium severity findings. |
| » low | number(float)¦null | false | The bounty multiplier for low severity findings. |
| » bounty_pool_limit | integer¦null | false | The maximum bounty pool budget for the campaign. |
| » start_date | string(date-time)¦null | false | The start date of the campaign. |
| » end_date | string(date-time)¦null | false | The end date of the campaign. |
| » status | string | true | The current status of the campaign. |
| » target_audience | boolean¦null | false | Whether the campaign targets a specific audience. |
| » extended_at | string(date-time)¦null | false | The date when the campaign was extended. |
| » total_reports | integer¦null | false | The total number of reports submitted during the campaign. |
| » valid_reports | integer¦null | false | The number of valid reports submitted during the campaign. |
| » total_critical_reports | integer¦null | false | The number of critical severity reports submitted during the campaign. |
| » total_high_reports | integer¦null | false | The number of high severity reports submitted during the campaign. |
| » bounty_spent | number(float)¦null | false | The total bounty amount spent during the campaign. |
| relationships | object | false | none |
| » campaign_objective | object | false | none |
| »» data | [campaign_objective](https://api.hackerone.com/customer-reference#campaign_objective) | false | A campaign objective defines the goal and target audience of a campaign. |
| » structured_scopes | object | false | none |
| »» data | [[structured-scope](https://api.hackerone.com/customer-reference#structured-scope)] | false | [A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program.] |
| » bounty_table_row | object¦null | false | none |
| »» data | object | false | none |
| »»» id | string | false | none |
| »»» type | string | false | none |
| »»» attributes | object | false | none |
| »»»» low | integer¦null | false | none |
| »»»» medium | integer¦null | false | none |
| »»»» high | integer¦null | false | none |
| »»»» critical | integer¦null | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| type | campaign |
| status | scheduled |
| status | active |
| status | inactive |
| type | bounty-table-row |

## campaign_objective

```
{
  "id": "string",
  "type": "campaign-objective",
  "attributes": {
    "name": "string",
    "description": "string",
    "category": "string",
    "key": "string",
    "target_audience_description": "string",
    "asset_types": [
      "string"
    ]
  }
}

```

Last revised: 2026-04-10

A campaign objective defines the goal and target audience of a campaign.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the campaign objective. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The name of the campaign objective. |
| » description | string | false | A description of the campaign objective. |
| » category | string¦null | false | The category of the campaign objective. |
| » key | string | true | The unique key identifier of the campaign objective. |
| » target_audience_description | string¦null | false | A description of the target audience for this objective. |
| » asset_types | [string]¦null | false | The asset types applicable to this objective. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | campaign-objective |

## collaborator

```
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
}

```

Last revised: 2023-10-05

A User who participated in a report with their respective collaboration weight.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| weight | number | true | The collaborator weight in the report. |
| user | [user](https://api.hackerone.com/customer-reference#user) | true | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

## credential

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

Last revised: 2023-07-11

A credential object contains the information that is associated to a credential

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the category. |
| type | string | true | none |
| attributes | object | true | none |
| » credentials | object | true | none |
| »» table | object | false | The information to be provided to the assigned hacker |
| » revoked | boolean | true | Indicates if the credential has been revoked. Revoked credentialscannot be used to access the target. |
| » account_details | string | false | The account details of the credential. |
| » assignee_id | string | false | The ID of the user that the credential is assigned to. |
| » assignee_username | string | false | The username of the user that the credential is assigned to. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | credential |

## credential_inquiry

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

Last revised: 2025-06-10

A credential inquiry object contains the information that is associated to a credential inquiry

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the credential inquiry |
| type | string | true | none |
| attributes | object | true | none |
| » description | string | true | The information to be requested from the hacker |

Enumerated Values

| Property | Value |
| --- | --- |
| type | credential_inquiry |

## credential_inquiry_response

```
{
  "id": "string",
  "type": "credential_inquiry_response",
  "attributes": {
    "details": "string",
    "user_id": "string",
    "created_at": "2019-08-24T14:15:22Z"
  }
}

```

Last revised: 2025-06-10

A credential inquiry response object contains the information that is associated to a credential inquiry response

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the credential inquiry response |
| type | string | true | none |
| attributes | object | true | none |
| » details | string | false | The information provided from the hacker |
| » user_id | string | false | The ID of the user that created the credential inquiry response. |
| » created_at | string(date-time) | false | The date and time the credential inquiry response was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | credential_inquiry_response |

## custom-field-attribute

```
{
  "id": "1337",
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

```

Last revised: 2021-06-25

A Custom Field Attribute is an object containing the label and configuration of a Custom Field created for a Report or Program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the custom field attribute. |
| type | string | true | none |
| attributes | object | true | none |
| » label | string | true | The attribute's label. |
| » field_type | string | false | The type of custom field |
| » internal | boolean | false | Internal or public custom field |
| » required | boolean | false | Is the field required? |
| » regex | string¦null | false | A regex used to validate the input for a text field |
| » error_message | string¦null | false | A custom error message when the regex validation fails |
| » checkbox_text | string¦null | false | The text shown with a checkbox field |
| » configuration | string¦null | false | An optional configuration for the attribute's type. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| » archived_at | string(date-time)¦null | false | The date and time the object was archived. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | custom-field-attribute |

## custom-field-input

```
{
  "id__eq": "1",
  "value__eq": "Infrastructure"
}

```

Last revised: 2021-06-25

An input to query for Report types by Custom Fields IDs and values.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id__eq | string | true | The ID of the Custom Field Attribute that needs to be filtered by. |
| value__eq | string | true | The Value of the corresponding Custom Field Value object that needs to befiltered by. Wildcards (% and _) can be used to loosely match on the storedvalue of the Custom Field. |

## custom-field-value

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

Last revised: 2021-06-25

A Custom Field Value object contains the value set for a particular Custom Field Attribute.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the custom field value. |
| type | string | true | none |
| attributes | object | true | none |
| » value | string¦null | true | The attribute's value. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » custom_field_attribute | object | true | none |
| »» data | [custom-field-attribute](https://api.hackerone.com/customer-reference#custom-field-attribute) | false | The Custom Field Attribute associated with theCustom Field Value object. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | custom-field-value |

## custom-remediation-guidance

```
{
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

```

Last revised: 2021-06-25

Custom remediation guidance that has been written by a team member.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the custom remediation guidance. |
| type | string | true | Indicates what kind of object it is. |
| attributes | object | true | none |
| » message | string | true | The text content of the custom remediation guidance. |
| » created_at | string(date-time) | true | The date and time the custom remediation guidance was created.Formatted according to ISO 8601. |
| relationships | object | true | none |
| » author | object | true | The user that wrote or last edited the custom remediation guidance. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

## cve-request

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

Last revised: 2026-02-12

This object contains the information that was submitted to request a new CVE for a program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the cve request |
| type | string | true | none |
| attributes | object | true | none |
| » request_type | string | true | The type of request. Possible values are "new" or "update". |
| » team_handle | string | true | The handle of the team. |
| » state | string | true | The state of the request. Possible values are "draft", "pending_hackerone_approval", \ "hackerone_approved", "pending_mitre_approval", "mitre_approved", "cancelled". |
| » versions | [object] | true | none |
| »» vendor | string | true | The vendor of the version. |
| »» product | string | true | The product of the version. |
| »» func | string | true | The function of the version. |
| »» version | string | true | The version. |
| »» versionUpperBound | string | false | The upper bound version. Optional field that specifies the end of a version range. If not provided or empty, defaults to the value of 'version'. |
| »» versionType | string | true | The type of the version. |
| »» affected | boolean | true | Whether the version is affected or not. |
| » metrics | [object] | true | none |
| »» vectorString | string | true | The vector string. |
| » weakness_name | string¦null | false | The name of the weakness. |
| » description | string | true | Description of the information required from the hackers to create a CVE request. |
| » latest_state_change_reason | string¦null | false | The reason for the latest state change. |
| » cve_identifier | string¦null | false | The identifier of the CVE. |
| » auto_submit_on_publicly_disclosing_report | boolean¦null | false | Whether the request should be auto submitted on publicly disclosing report or not. Default is false. |
| » vulnerability_discovered_at | string(date-time) | true | The date when the vulnerability was discovered. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted according to ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | cve-request |

## email_message

```
{
  "data": {
    "success": true,
    "message": "Email successfully sent"
  }
}

```

Last revised: 2025-01-28

Attributes that define an email message

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| type | string | false | none |
| attributes | object | false | none |
| required | any | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| type | email-message |

## error

```
{
  "status": 0,
  "title": "string",
  "detail": "string",
  "source": {
    "parameter": "string"
  }
}

```

Last revised: 2025-06-10

Error objects represent problem responses for API requests that contain status codes, error messages and additional details.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| status | integer | true | The HTTP status code. |
| title | string | false | The error message. |
| detail | string | false | Additional details about the error. |
| source | object | false | none |
| » parameter | string | false | The name of the parameter related to the error. |

## errors

```
{
  "errors": [
    {
      "status": 0,
      "title": "string",
      "detail": "string",
      "source": {
        "parameter": "string"
      }
    }
  ]
}

```

Last revised: 2025-06-10

Collection of error objects returned by the API when a request fails.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| errors | [[error](https://api.hackerone.com/customer-reference#error)] | true | Array of error objects. |

## group

```
{
  "id": "1337",
  "type": "group",
  "attributes": {
    "name": "Admin",
    "created_at": "2016-02-02T04:05:06.000Z",
    "permissions": [
      "user_management",
      "report_management"
    ]
  }
}

```

Last revised: 2021-06-25

A group represents a set of users. A group is used to delegate permissions for the users in it. It can also be assigned to one or multiple reports.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the group. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The name of the group. |
| » permissions | [string] | true | The permissions of the group. Possible values are reward_management,program_management, user_management, andreport_management. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | group |

## hai-completion

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

Last revised: 2024-05-22

A completion is generated when a user communicates with Hai. Hai will then generate a response to the user's question.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the completion. |
| type | string | true | Indicates what kind of object it is. |
| attributes | object | true | none |
| » state | string | true | The state of the completion. |
| » created_at | string(date-time) | true | The time the completion was created. |
| » response | string¦null | false | The response to the question. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | completion |
| state | generating |
| state | created |
| state | partially_completed |
| state | completed |
| state | cancelled |
| state | failed |

## inbox

```
{
  "data": {
    "id": "84",
    "type": "inbox",
    "attributes": {
      "message": "ACME program inbox.",
      "type": "default"
    }
  }
}

```

Last revised: 2024-02-08

An inbox object represents an inbox that belongs to an organization and holds a set of reports. Default (aka program inboxes) are created by the system and cannot be deleted and hold all reports of the program Custom inboxes are created by the user and can be deleted and hold only reports that are explicitly assigned to them.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the inbox object. |
| type | string | true | Indicates what kind of object it is. |
| attributes | object | true | none |
| » type | string | true | The type of the inbox. Possible values:`custom`,`default`,`summary`. |
| » name | string | true | The name of the inbox. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | inbox |

## invitation

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  }
}

```

Last revised: 2021-06-25

These objects represent an invitation that was sent to a recipient. Invitations come in many sub types that can have additional attributes.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the invitation. |
| type | string | true | Indicates what kind of invitation it is. |
| attributes | object | true | none |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |

## invitation-hacker

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
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

Last revised: 2025-03-25

Hacker invitation objects represent invitations that have been issued from a private program on HackerOne. These are invitations to your program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| invitation-hacker | any | false | Hacker invitation objects represent invitations that have been issued from a private program on HackerOne.These are invitations to your program. |

allOf

Last revised: 2025-03-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [invitation](https://api.hackerone.com/customer-reference#invitation) | false | These objects represent an invitation that was sent to a recipient.Invitations come in many sub types that can have additional attributes. |

and

Last revised: 2025-03-25

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » id | string | true | The unique ID of the invitation. |
| » type | string | true | none |
| » attributes | object | true | none |
| »» state | string¦null | false | The status of the invitation. |
| »» created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| »» viewed_at | string(date-time)¦null | false | The date and time the invitation was viewed. Formatted accordingto ISO 8601. |
| »» accepted_at | string(date-time)¦null | false | The date and time the invitation was accepted. Formatted accordingto ISO 8601. |
| »» expires_at | string(date-time)¦null | false | The date and time the invitation expires. Formatted accordingto ISO 8601. |
| »» rejected_at | string(date-time)¦null | false | The date and time the invitation was rejected. Formatted accordingto ISO 8601. |
| »» cancelled_at | string(date-time)¦null | false | The date and time the invitation was cancelled. Formatted accordingto ISO 8601. |
| » relationships | object | true | none |
| »» recipient | [user](https://api.hackerone.com/customer-reference#user) | false | the user who the invitation is issued to. |
| »» invited_by | [user](https://api.hackerone.com/customer-reference#user) | false | the user who sent the invitation. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | invitation-hacker |

## invitation-organization-member

```
{
  "id": "string",
  "type": "string",
  "attributes": {
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  },
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

Last revised: 2024-08-15

These objects represent an invitation that was sent to a recipient to become an organization member.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| invitation-organization-member | any | false | These objects represent an invitation that was sent to a recipient to become an organization member. |

allOf

Last revised: 2024-08-15

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [invitation](https://api.hackerone.com/customer-reference#invitation) | false | These objects represent an invitation that was sent to a recipient.Invitations come in many sub types that can have additional attributes. |

and

Last revised: 2024-08-15

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » id | string | true | The unique ID of the organization_member_group. |
| » type | string | true | none |
| » attributes | object | true | none |
| »» email | string¦null | false | The email of the invited user.Returned if the user email is public. |
| »» username | string¦null | false | The username of the invited user is deprecated and will always return null. |
| »» invited_by_id | string | true | The unique ID of the invitee user. |
| »» recipient_id | string¦null | false | The unique ID of the invited user is deprecated and will always return null. |
| »» invitation_data | object | true | Additional data for the invitation. |
| »»» notify | boolean | false | Activates organization notifications for the user you are inviting. |
| »»» organization_admin | boolean | false | Sets the user you are inviting as an organization admin. |
| »»» organization_member_group_ids | [string] | false | The unique ids of the groups where the user is invited.The user's email must be respect the eligibility settings of these groups. |
| »» expires_at | string(date-time) | false | The date and time the organization member invitation expires. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | invitation-organization-member |

## invitation-report

```
{
  "id": "117",
  "type": "report-participant",
  "attributes": {
    "created_at": "2016-02-02T04:05:06.000Z",
    "updated_at": "2016-02-02T04:05:06.000Z",
    "report_id": "1337"
  }
}

```

Last revised: 2024-02-08

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| invitation-report | any | false | none |

allOf

Last revised: 2024-02-08

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | [invitation](https://api.hackerone.com/customer-reference#invitation) | false | These objects represent an invitation that was sent to a recipient.Invitations come in many sub types that can have additional attributes. |

and

Last revised: 2024-02-08

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| anonymous | object | false | none |
| » attributes | object | true | none |
| »» report_id | string | true | The ID of the report associated with the invitation. |

## links

```
{
  "data": [
    {
      "id": "1337",
      "type": "some-object",
      "attributes": {
        "some_attribute": "some value"
      },
      "relationships": {
        "some_relationship": {
          "data": {
            "id": "1337",
            "type": "some-other-object",
            "attributes": {
              "some_attribute": "some value"
            }
          }
        }
      }
    }
  ],
  "links": {
    "first": "https://api.hackerone.com/v1/reports/1333",
    "prev": "https://api.hackerone.com/v1/reports/1336",
    "self": "https://api.hackerone.com/v1/reports/1337",
    "next": "https://api.hackerone.com/v1/reports/1338",
    "last": "https://api.hackerone.com/v1/reports/1345"
  }
}

```

Last revised: 2025-06-10

When querying for multiple objects, the client needs to know how to query the next page. This kind of data is included in this attribute. In case there is no additional meta data, this attribute is not returned by the API.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| attributes | object | false | none |
| » first | string | false | This attribute contains a URL to the first page or first resource when the resourceor resources are paginated. |
| » prev | string | false | This attribute contains a URL to the previous page or previous resource whenthe resource or resources are paginated. |
| » self | string | false | This attribute contains a URL to the resource itself when it can be queried as atop level resource. At this moment, only report objects canbe queried as individual resources. |
| » next | string | false | This attribute contains the URL to the next page or next resource when the resourceor resources are paginated. |
| » last | string | false | This attribute contains a URL to the last page or last resource when the resourceor resources are paginated. |

## member

```
{
  "id": "1337",
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

```

Last revised: 2025-06-10

A member represents a user that is part of a program. A member is used to delegate permissions for the users attached to it.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the member. |
| type | string | true | none |
| attributes | object | true | none |
| » permissions | [string] | true | The permissions of the member. Possible values are reward_management,program_management, user_management, andreport_management. |
| » groups | [object] | false | The list of groups the member belongs to. |
| »» data | [[group](https://api.hackerone.com/customer-reference#group)] | false | [A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports.] |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| relationships | object | true | none |
| » user | object | true | The user that is part of the program. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | true | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | member |

## organization

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

Last revised: 2022-09-08

An organization object represents an organization on the platform. When [a user](https://api.hackerone.com/customer-reference#user) wants to know about organization assets, this is the object they interact with. Behind an organization, there can be multiple users that are part of the organization.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the organization. |
| type | string | true | none |
| attributes | object | true | none |
| » handle | string | true | The handle of the organization. Handles are unique and scoped under the samenamespace as user usernames. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | organization |

## asset

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

An asset object represents an asset defined by the organization. Organization assets can be added to program scope where a related StructuredScope object is created.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the asset. |
| type | string | true | none |
| attributes | object | true | none |
| » asset_type | string | true | The type of the asset |
| » domain_name | string | false | The identifier of the asset. Only for asset type domain. Alias for`identifier`. |
| » url | string | false | The url of the asset. Only for asset type url. Alias for`identifier`. |
| » block | string | false | The IPv4 or IPv6 address of the asset. Only for asset type cidr. Alias for`identifier`. |
| » identifier | string | true | The identifier of the asset. |
| » available_from | string(date-time) | false | The date and time the asset was is available from updated. Formatted accordingto ISO 8601. Only for asset types sourceCode. Alias for`identifier`. |
| » app_store_id | string | false | The app store ID of the asset.Only for asset types iosAppStore, iosTestflight, iosIpa, androidPlayStore, androidApk, windowsMicrosoftStore. Alias for`identifier`. |
| » description | string¦null | false | The asset description. |
| » coverage | string | false | The asset coverage by programs. |
| » state | [asset-states](https://api.hackerone.com/customer-reference#asset-states) | true | The asset's current state. |
| » owner | string¦null | false | The asset owner. |
| » max_severity | string¦null | false | The qualitative rating of the maximum severity allowed on this asset |
| » confidentiality_requirement | string | false | A CVSS environmental modifier that reweights Confidentiality Impactof a vulnerability on this asset. |
| » integrity_requirement | string | false | A CVSS environmental modifier that reweights Integrity Impact of avulnerability on this asset. |
| » availability_requirement | string | false | A CVSS environmental modifier that reweights Availability Impact ofa vulnerability on this asset. |
| » created_at | string(date-time) | false | The date and time the asset was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | false | The date and time the asset was last updated. Formatted accordingto ISO 8601. |
| » archived_at | string(date-time)¦null | false | The date and time the asset was archived. Formatted accordingto ISO 8601. |
| » reference | string | false | The customer defined reference identifier or tag of the asset. |
| relationships | object | false | none |
| » asset_tags | object | false | A list of AssetTag objects assigned to the asset. |
| »» data | [[asset-tag-small](https://api.hackerone.com/customer-reference#asset-tag-small)] | false | [An asset tag object contains the information that is associated to an asset tag including relationships] |
| » programs | object | false | A list of Program objects that have the asset in scope or out of scope. |
| »» data | [[program](https://api.hackerone.com/customer-reference#program)] | false | [A program object represents a disclosure program or bug bounty program on theplatform. When [a user](https://api.hackerone.com/customer-reference#user) reports a bug to a program, this isthe object they interact with. Behind a program, there can be multiple usersthat are part of the program. Those users can interact with reports on behalfof the program.] |
| » attachments | object | false | A list of Attachment objects that belong to the asset. |
| »» data | [[attachment](https://api.hackerone.com/customer-reference#attachment)] | false | [Users can add attachments when they file a report or when they interact with areport. Attachments may contain dangerous proof of concepts and should be handledwith caution.] |
| » asset_ports | object | false | A list of open ports discovered on the asset. |
| »» data | [[asset-port](https://api.hackerone.com/customer-reference#asset-port)] | false | [An asset port object represents an open port discovered on an asset.] |
| » reachability | object | false | Reachability status and information for the asset. |
| »» data | [asset-reachability](https://api.hackerone.com/customer-reference#asset-reachability) | false | Reachability status and information for an asset. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset |
| asset_type | domain |
| asset_type | url |
| asset_type | cidr |
| asset_type | hardware |
| asset_type | sourceCode |
| asset_type | iosAppStore |
| asset_type | iosTestflight |
| asset_type | iosIpa |
| asset_type | androidPlayStore |
| asset_type | androidApk |
| asset_type | windowsMicrosoftStore |
| asset_type | executable |
| asset_type | other |
| asset_type | smartContract |
| asset_type | api |
| asset_type | aiModel |
| asset_type | awsCloudConfig |
| asset_type | azureCloudConfig |
| coverage | in_scope |
| coverage | out_of_scope |
| coverage | untested |
| max_severity | none |
| max_severity | low |
| max_severity | medium |
| max_severity | high |
| max_severity | critical |
| confidentiality_requirement | none |
| confidentiality_requirement | low |
| confidentiality_requirement | medium |
| confidentiality_requirement | high |
| integrity_requirement | none |
| integrity_requirement | low |
| integrity_requirement | medium |
| integrity_requirement | high |
| availability_requirement | none |
| availability_requirement | low |
| availability_requirement | medium |
| availability_requirement | high |

## asset-import

```
{
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

```

Last revised: 2026-01-29

An asset import object contains the information that is associated to an asset import including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | int | true | The unique ID of the asset import. |
| type | string | true | none |
| attributes | object | true | none |
| » state | string | true | - created - a new asset import is created and/or scheduled for execution.- importing - asset import is being processed.- failed - importing failed.- processed - importing finished without any errors.- processed_with_error - importing finished, but there are invalid identifiers in the import file. |
| » errors | array | false | The identifier of the asset. Only for asset type domain. |
| » created_at | string(date-time) | true | The date and time the asset was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the asset was last updated. Formatted accordingto ISO 8601. |
| » processed_new_ids | [integer] | false | Array of asset IDs that were created during this import. |
| » processed_existing_ids | [integer] | false | Array of asset IDs that already existed before this import. |
| » source | string | true | Identifies the origin of the import:- AssetScanner - Automated scanner run- ManualImport - Manual CSV upload- OrganizationAPI - API-initiated import- AssetSubmission - Hacker-submitted assets- AssetInventory - Asset inventory sync- HackerAPI - Hacker API submission- DarktraceIntegration - Darktrace integration (renamed to scanner on export)- PullRequestSync - Pull request synchronization- Unknown - Legacy or unspecified |
| » processed_updated_ids | [integer] | false | Array of asset IDs that existed and were modified during this import.These are assets that had metadata changes. |
| » processed_unchanged_ids | [integer] | false | Array of asset IDs that existed but had no changes during this import.Computed as: processed_existing_ids minus processed_updated_ids. |
| » archived_ids | [integer] | false | Array of asset IDs that were archived during this import. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-import |
| state | created |
| state | importing |
| state | failed |
| state | processed |
| state | processed_with_errors |
| source | AssetSubmission |
| source | AssetInventory |
| source | AssetScanner |
| source | HackerAPI |
| source | ManualImport |
| source | OrganizationAPI |
| source | DarktraceIntegration |
| source | PullRequestSync |
| source | Unknown |

## asset-import-csv-format

```
[
  "identifier;asset_type;state;max_severity;description;technologies;port hackerone.com;Domain;Confirmed;critical;\"Main production website\";Ruby,Rails;80/tcp,443/tcp 192.168.1.0/24;Cidr;New;high;\"Internal network\";;22/tcp api.hackerone.com;Domain;Confirmed;critical;\"REST API\";Node.js,GraphQL;443/tcp"
]

```

Last revised: 2026-01-28

CSV file format specification for bulk asset imports.

#### File Requirements

- [Reference](https://api.hackerone.com/hacker-reference)
- Separator: Semicolon (`;`)
- File Size: Maximum 15 megabytes
- MIME Types:`text/csv` or`application/vnd.ms-excel`
- Encoding: UTF-8 (BOM encoding supported)
- Processing: Asynchronous (batch processing, 100 assets per batch)
- Header Row: Required - first row must contain field names

#### Processing States

After import, check the`state` field of the asset-import response object.

- created - Import scheduled for execution
- importing - Assets being processed
- processed - All assets imported successfully
- processed_with_errors - Some assets had errors (check errors array)
- failed - Import failed completely

#### Error Handling

Common Errors:

- Invalid identifier format for the specified asset_type
- Duplicate identifier (asset already exists)
- Invalid asset_type value
- Invalid enum value for fields
- Invalid port format (out of range or invalid protocol)
- File too large (exceeds 15MB limit)
- Invalid MIME type (not recognized as CSV)

#### Best Practices

Performance: Import processes 100 assets per batch. Large imports (1000+ assets) will take several minutes. Poll the GET endpoint to check status.

Data Quality: Identifiers are auto-normalized based on asset_type. Validate data before import and test with a small batch first.

Security: Avoid sensitive information in description/reference fields. Use`New` state for unverified assets,`Confirmed` only for verified, in-scope assets.

#### API Response Example

After uploading a CSV file, the API returns an asset-import object. To check the import status, poll the GET endpoint using the`id` from the response. When processing completes, the`state` will change to`processed` or`processed_with_errors`.

```
#Checking Import Status - Completed Response

{
  "data": {
    "id": "12345",
    "type": "asset-import",
    "attributes": {
      "state": "processed",
      "errors": [],
      "created_at": "2024-01-20T10:30:00Z",
      "updated_at": "2024-01-20T10:35:00Z",
      "processed_new_ids": [1001, 1002],
      "processed_existing_ids": [501, 502]
    }
  }
}

```

```
#Checking Import Status - Partial Success
{
  "data": {
    "id": "12345",
    "type": "asset-import",
    "attributes": {
      "state": "processed_with_errors",
      "errors": [
        "Missing identifier on line 5",
        "Invalid asset type \"InvalidType\" on line 12"
      ],
      "created_at": "2024-01-20T10:30:00Z",
      "updated_at": "2024-01-20T10:35:00Z",
      "processed_new_ids": [1001],
      "processed_existing_ids": [501]
    }
  }
}

```

```
#Checking Import Status - Completed Failure

{
  "data": {
    "id": "12345",
    "type": "asset-import",
    "attributes": {
      "state": "failed",
      "errors": [
        "Invalid column separator `,` -- please use `;` as a separator instead"
      ],
      "created_at": "2024-01-20T10:30:00Z",
      "updated_at": "2024-01-20T10:35:00Z",
      "processed_new_ids": [],
      "processed_existing_ids": []
    }
  }
}

```

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| identifier | string | true | Asset identifier (domain, URL, IP, etc.)Format: Varies by asset typeExamples:- Domain: hackerone.com- URL: https://api.hackerone.com- CIDR: 192.168.1.0/24- IP Address: 192.168.1.1- iOS App Store: com.hackerone.mobile- Android Play Store: com.hackerone.androidValidation: Cannot be blank |
| asset_type | string | false | Type of asset being importedDefault: Domain if not specifiedSupported Values: Domain, Url, Wildcard, AndroidPlayStore, AndroidApk, OtherAsset, Hardware, SourceCode, WindowsMicrosoftStore, IosAppStore, IosIpa, IosTestflight, Executable, Cidr, SmartContract, AiModel, Api, AwsCloudConfig, AzureCloudConfig |
| description | string | false | Asset descriptionMax Length: 25,000 charactersExample: Main production website |
| reference | string | false | Reference identifier or external IDMax Length: 255 charactersExample: ASSET-12345 |
| state | string | false | Asset confirmation stateDefault: ConfirmedSupported Values:- Confirmed - Asset is confirmed- New - Asset requires reviewCase-Insensitive: Yes |
| source | string | false | External source identifierExample: External Vendor, Security TeamNote: Used for tracking, not validation |
| max_severity | string | false | Maximum severity rating allowed for vulnerabilitiesDefault: criticalSupported Values: critical, high, medium, low, noneCase-Insensitive: Yes |
| confidentiality_requirement | string | false | CVSS environmental score modifier for confidentialitySupported Values: high, medium, lowCase-Insensitive: Yes |
| integrity_requirement | string | false | CVSS environmental score modifier for integritySupported Values: high, medium, lowCase-Insensitive: Yes |
| availability_requirement | string | false | CVSS environmental score modifier for availabilitySupported Values: high, medium, lowCase-Insensitive: Yes |
| port | string | false | Port specifications for the assetFormats:- Simplified: "80,443" (defaults to TCP)- Full format: "80/tcp,443/tcp,53/udp"- Mixed: "80,443/tcp,53/udp"Parsing:- Port numbers must be 1-65535- Protocol must be tcp or udp- Comma-separated listLimit: 100 ports per assetExamples:- 80,443 → Creates TCP ports 80 and 443- 80/tcp,443/tcp,53/udp → Creates TCP 80, TCP 443, UDP 53- 22 → Creates TCP port 22 |
| technologies | string | false | Technology tags (comma-separated)Format: Comma-separated tag namesExample: Node.js,React,PostgreSQLBehavior:- Automatically creates "Technology" tag category if not exists- Creates individual tags if they don't exist- Associates tags with the asset |
| site_status | string | false | Site status tagExample: Active, Staging, DeprecatedBehavior:- Automatically creates "Site Status" tag category if not exists- Creates tag if it doesn't exist- Associates tag with the asset |
| risk_rating | string | false | Risk rating tagSupported Values: A (only "A" is currently accepted)Case-Insensitive: YesBehavior:- Automatically creates "Risk Rating" tag category if not exists- Associates with the asset |
| geo_country | string | false | Geographic region/country tagExample: US, EU, APACBehavior:- Automatically creates "Region" tag category if not exists- Creates tag if it doesn't exist- Associates tag with the asset |

## asset-port

```
{
  "id": "string",
  "type": "asset-port",
  "attributes": {
    "port": 1,
    "protocol": "string",
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  }
}

```

Last revised: 2026-01-29

An asset port object represents an open port discovered on an asset.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the asset port. |
| type | string | true | none |
| attributes | object | true | none |
| » port | integer | true | The port number. |
| » protocol | string | true | The protocol (e.g., tcp, udp). |
| » created_at | string(date-time) | false | The date and time the port was discovered. |
| » updated_at | string(date-time) | false | The date and time the port information was last updated. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-port |

## asset-reachability

```
{
  "id": "string",
  "type": "asset-reachability",
  "attributes": {
    "last_status": "string",
    "refreshable": true,
    "updated_at": "2019-08-24T14:15:22Z"
  }
}

```

Last revised: 2026-01-29

Reachability status and information for an asset.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the reachability record. |
| type | string | true | none |
| attributes | object | true | none |
| » last_status | string | true | The last reachability status (e.g., reachable, unreachable). |
| » refreshable | boolean | true | Whether the reachability can be refreshed. |
| » updated_at | string(date-time) | false | The date and time the reachability was last checked. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-reachability |

## asset-screenshot

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

Last revised: 2024-02-08

An asset screenshot object contains the information about the screenshot

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The unique ID of the asset_screenshot. |
| type | string | true | none |
| attributes | object | true | none |
| » file_name | string | true | The file name of the asset screenshot |
| » content_type | string | true | The content type of the asset screenshot. The content type is derived from thecontents and extension of the file. |
| » file_size | integer | true | The file size of the asset_screenshot in bytes. |
| » expiring_url | string | true | A URL to download the asset screenshot. The URL will automatically expire after60 minutes. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-screenshot |

## asset-states

```
"confirmed"

```

Last revised: 2024-02-08

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| asset-states | string | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| asset-states | confirmed |
| asset-states | rejected |
| asset-states | unconfirmed |

## asset-tag

```
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

```

Last revised: 2024-05-08

An asset tag object contains the information that is associated to an asset tag including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the asset tag. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The name of the asset tag |
| relationships | object | true | none |
| » asset_tag_category | object | true | The AssetTagCategory object assigned to the asset tag. |
| »» data | [asset-tag-category](https://api.hackerone.com/customer-reference#asset-tag-category) | true | An asset tag category object contains the information that is associated to an asset tag category |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-tag |

## asset-tag-category

```
{
  "id": "2",
  "type": "asset-tag-category",
  "attributes": {
    "name": "test"
  }
}

```

Last revised: 2024-02-27

An asset tag category object contains the information that is associated to an asset tag category

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the asset tag category. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The unique name of the asset tag category. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-tag-category |

## asset-tag-small

```
{
  "id": "2",
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

```

Last revised: 2024-02-27

An asset tag object contains the information that is associated to an asset tag including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the asset tag. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The name of the asset tag |
| relationships | object | true | none |
| » asset_tag_category | object | true | The AssetTagCategory object assigned to the asset tag. |
| »» data | [asset-tag-category](https://api.hackerone.com/customer-reference#asset-tag-category) | true | An asset tag category object contains the information that is associated to an asset tag category |

Enumerated Values

| Property | Value |
| --- | --- |
| type | asset-tag |

## eligibility-setting

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

Last revised: 2024-02-08

An eligibility setting object contains the information that is associated to an organization eligibility settings including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the eligibility setting. |
| type | string | true | none |
| attributes | object | true | none |
| » organization_id | string | true | The unique ID of the organization. |
| » name | string | true | The name of the eligibility setting. |
| » allowed_domains | array | true | The list of allowed domains for the eligibility setting. |
| » allowed_domains_enabled | boolean | true | Indicates if the eligibility setting is enabled for the allowed domains. |
| » created_at | string(date-time) | true | The date and time the eligibility setting was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the eligibility setting was last updated. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | eligibility-setting |

## organization-member

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

An organization member object contains the information that is associated to an organization members including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the organization member. |
| type | string | true | none |
| attributes | object | true | none |
| » organization_id | string | true | The unique id of the organization. |
| » user_id | string | true | The unique id of the user. |
| » email | string | false | The email of the organization member. |
| » organization_admin | boolean | false | Indicates if the user is an organization admin. |
| » created_at | string(date-time) | false | The date and time the organization member was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | false | The date and time the organization member was last updated. Formatted accordingto ISO 8601. |
| » last_sign_in_at | string(date-time) | false | The date and time of the user's most recent sign-in. Formatted according to ISO 8601. |
| » system | boolean | false | Indicates if the organization member is a system user. |
| » username | string | false | The username of the organization member. |
| relationships | object | false | none |
| » organization_member_groups | object | false | List of organization member groups user belongs to. |
| »» data | [[organization-member-group](https://api.hackerone.com/customer-reference#organization-member-group)] | false | [An organization member group object contains the information that is associated to an organization members group including relationships] |

Enumerated Values

| Property | Value |
| --- | --- |
| type | organization-member |

## organization-member-group

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

Last revised: 2024-09-10

An organization member group object contains the information that is associated to an organization members group including relationships

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the organization member group. |
| type | string | true | none |
| attributes | object | true | none |
| » organization_id | string | true | The unique id of the organization. |
| » eligibility_setting_id | string¦null | false | The unique id of the eligibility setting. |
| » name | string | true | The name of the group. |
| » permissions | [string] | false | The permissions of the organization member group. Possible values are: asset_inventory_manager, asset_inventory_viewer, group_manager, program_admin, read_only_member, report_analyst, report_reward_managerand user_manager. |
| » created_at | string(date-time) | true | The date and time the organization member group was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the organization member group was last updated. Formatted accordingto ISO 8601. |
| » migrated_at | string(date-time)¦null | false | The date and time the organization member group was migrated. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » organization_members | object | false | List of organization members. |
| »» data | [[organization-member](https://api.hackerone.com/customer-reference#organization-member)] | false | [An organization member object contains the information that is associated to an organization members including relationships] |
| » programs | object | false | none |
| »» data | [object] | false | none |
| »»» id | string | false | The unique ID of the program. |
| »»» type | string | false | none |
| »»» attributes | object | false | none |
| »»»» handle | string | true | The handle of the program. Handles are unique and scoped under the samenamespace as user usernames. |
| »»»» created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| »»»» updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| » inboxes | object | false | List of organization inboxes. |
| »» data | [[inbox](https://api.hackerone.com/customer-reference#inbox)] | false | [An inbox object represents an inbox that belongs to an organization and holds a set of reports.Default (aka program inboxes) are created by the system and cannot be deleted and hold all reports of the programCustom inboxes are created by the user and can be deleted and hold only reports that are explicitly assigned to them.] |

Enumerated Values

| Property | Value |
| --- | --- |
| type | organization-member-group |
| type | program |

## program

```
{
  "id": "1337",
  "type": "program",
  "attributes": {
    "handle": "security",
    "policy": "The policy of the program.",
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
    "custom_field_attributes": {
      "data": [
        {
          "id": "1337",
          "type": "custom-field-attribute",
          "attributes": {
            "label": "Team",
            "configuration": null,
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z",
            "archived_at": null
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
    "policy_attachments": {
      "data": [
        {
          "id": "<id>",
          "type": "attachment",
          "attributes": {
            "expiring_url": "<url>",
            "created_at": "2016-02-02T04:05:06.000Z",
            "file_name": "logo.png",
            "content_type": "image/png",
            "file_size": 3650
          }
        }
      ]
    }
  }
}

```

Last revised: 2024-05-01

A program object represents a disclosure program or bug bounty program on the platform. When [a user](https://api.hackerone.com/customer-reference#user) reports a bug to a program, this is the object they interact with. Behind a program, there can be multiple users that are part of the program. Those users can interact with reports on behalf of the program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the program. |
| type | string | true | none |
| attributes | object | true | none |
| » handle | string | true | The handle of the program. Handles are unique and scoped under the samenamespace as user usernames. |
| » policy | string | true | The policy of the program. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » groups | object | false | The groups of the program, which is used to delegate permissions andcan be used to assign multiple users to a single report. Only includedwhen the program object is fetched through the program resource. |
| »» data | [[group](https://api.hackerone.com/customer-reference#group)] | false | [A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports.] |
| » members | object | false | The members of the program, which is used to define the permissions ofa user's membership of a program. Only included when the program objectis fetched through the program resource. |
| »» data | [[member](https://api.hackerone.com/customer-reference#member)] | false | [A member represents a user that is part of a program. A member is used to delegate permissionsfor the users attached to it.] |
| » policy_attachments | object | false | Policy attachments of the program. Only included when the program objectis fetched through the program resource. |
| »» data | [[attachment](https://api.hackerone.com/customer-reference#attachment)] | false | [Users can add attachments when they file a report or when they interact with areport. Attachments may contain dangerous proof of concepts and should be handledwith caution.] |
| » custom_field_attributes | object | false | The Custom Field Attributes of the program, which are used to defineCustom Fields on a Report. |
| »» data | [[custom-field-attribute](https://api.hackerone.com/customer-reference#custom-field-attribute)] | false | [A Custom Field Attribute is an object containing the label and configurationof a Custom Field created for a Report or Program.] |
| » transactions | object | false | The payment transactions of the program for the selected period. |
| »» data | [[transaction](https://api.hackerone.com/customer-reference#transaction)] | false | [A Transaction object represents the information about the programpayment transaction.] |
| » organization | object | false | The organization this program belongs to. Only included when the programobject is fetched through the program resource. |
| »» data | object | false | none |
| »»» data | [organization](https://api.hackerone.com/customer-reference#organization) | false | An organization object represents an organization on the platform.When [a user](https://api.hackerone.com/customer-reference#user) wants to know about organization assets,this is the object they interact with. Behind an organization, there can be multipleusers that are part of the organization. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | program |

## program_integration

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

Last revised: 2024-08-21

Represents an integration associated with a program. Program integrations may include different types such as Jira, Manual, or Phabricator integrations.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the integration. |
| name | string | true | The name of the integration. |
| type | string | true | none |
| linkable | boolean | true | Indicates whether the integration is linkable. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | SolutionInstance |

## program_small

```
{
  "id": "1337",
  "type": "program",
  "attributes": {
    "handle": "security",
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
    "custom_field_attributes": {
      "data": [
        {
          "id": "1337",
          "type": "custom-field-attribute",
          "attributes": {
            "label": "Team",
            "configuration": null,
            "created_at": "2016-02-02T04:05:06.000Z",
            "updated_at": "2016-02-02T04:05:06.000Z",
            "archived_at": null
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
    "policy_attachments": {
      "data": [
        {
          "id": "<id>",
          "type": "attachment",
          "attributes": {
            "expiring_url": "<url>",
            "created_at": "2016-02-02T04:05:06.000Z",
            "file_name": "logo.png",
            "content_type": "image/png",
            "file_size": 3650
          }
        }
      ]
    }
  }
}

```

Last revised: 2021-06-29

A program object represents a disclosure program or bug bounty program on the platform. When [a user](https://api.hackerone.com/customer-reference#user) reports a bug to a program, this is the object they interact with. Behind a program, there can be multiple users that are part of the program. Those users can interact with reports on behalf of the program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the program. |
| type | string | true | none |
| attributes | object | true | none |
| » handle | string | true | The handle of the program. Handles are unique and scoped under the samenamespace as user usernames. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » groups | object | false | The groups of the program, which is used to delegate permissions andcan be used to assign multiple users to a single report. Only includedwhen the program object is fetched through the program resource. |
| »» data | [[group](https://api.hackerone.com/customer-reference#group)] | false | [A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports.] |
| » members | object | false | The members of the program, which is used to define the permissions ofa user's membership of a program. Only included when the program objectis fetched through the program resource. |
| »» data | [[member](https://api.hackerone.com/customer-reference#member)] | false | [A member represents a user that is part of a program. A member is used to delegate permissionsfor the users attached to it.] |
| » policy_attachments | object | false | Policy attachments of the program. Only included when the program objectis fetched through the program resource. |
| »» data | [[attachment](https://api.hackerone.com/customer-reference#attachment)] | false | [Users can add attachments when they file a report or when they interact with areport. Attachments may contain dangerous proof of concepts and should be handledwith caution.] |
| » custom_field_attributes | object | false | The Custom Field Attributes of the program, which are used to defineCustom Fields on a Report. |
| »» data | [[custom-field-attribute](https://api.hackerone.com/customer-reference#custom-field-attribute)] | false | [A Custom Field Attribute is an object containing the label and configurationof a Custom Field created for a Report or Program.] |
| » transactions | object | false | The payment transactions of the program for the selected period. |
| »» data | [[transaction](https://api.hackerone.com/customer-reference#transaction)] | false | [A Transaction object represents the information about the programpayment transaction.] |

Enumerated Values

| Property | Value |
| --- | --- |
| type | program |

## report

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

A report object contains the information that hackers submitted to a program, the interactions the program users had with the report, and all additional meta information like bounties, swag, and internal references.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the report. |
| type | string | true | none |
| attributes | object | true | none |
| » title | string | true | The title of the report. May be updated through the HackerOne interface. |
| » vulnerability_information | string | false | The raw report's vulnerability information. Markdown is not parsed. |
| » main_state | [report-main-states](https://api.hackerone.com/customer-reference#report-main-states) | true | The report's main state. Directly related to the state of the report. |
| » state | [report-states](https://api.hackerone.com/customer-reference#report-states) | true | The report's current state. May be updated through the HackerOne interface or [the HackerOne API](https://api.hackerone.com/customer-resources/#reports-change-state). |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » triaged_at | string(date-time)¦null | false | The date and time the report was triaged. This attribute is reset when thereport was reopened after it was triaged. Formatted according to ISO 8601. |
| » closed_at | string(date-time)¦null | false | The date and time the report was closed. This attribute is reset when thereport was reopened after it was closed. Formatted according to ISO 8601. |
| » last_reporter_activity_at | string(date-time)¦null | false | The date and time that the most recent reporter activity was posted on the report.Formatted according to ISO 8601. |
| » first_program_activity_at | string(date-time)¦null | false | The date and time that the first program activity was posted on the report.Formatted according to ISO 8601. |
| » last_program_activity_at | string(date-time)¦null | false | The date and time that the most recent program activity was posted on the report.Formatted according to ISO 8601. |
| » last_activity_at | string(date-time)¦null | false | The date and time that the most recent activity was posted on the report.Formatted according to ISO 8601. |
| » last_public_activity_at | string(date-time)¦null | false | The date and time that the most recent public activity was posted on the report.Formatted according to ISO 8601. |
| » bounty_awarded_at | string(date-time)¦null | false | The date and time that the most recent bounty was awarded on the report.Formatted according to ISO 8601. |
| » swag_awarded_at | string(date-time)¦null | false | The date and time that the most recent swag was awarded on the report.Formatted according to ISO 8601. |
| » disclosed_at | string(date-time)¦null | false | The date and time the report was disclosed. Formatted accordingto ISO 8601. |
| » reporter_agreed_on_going_public_at | string(date-time)¦null | false | The date and time the reporter agreed for the public disclosure.Formatted according to ISO 8601. |
| » issue_tracker_reference_id | string | false | The id of the issue tracker reference typically used whentriaging a report. |
| » issue_tracker_reference_url | string | false | The url of the issue tracker reference. |
| » cve_ids | [string] | false | An assigned CVE id(s) for this report |
| » source | string¦null | false | A free-form string defining the source of the report for tracking purposes.For example, "detectify", "rapid7" or "jira". |
| » timer_bounty_awarded_miss_at | date-time¦null | false | The date and time the system expects the program to have awarded a bounty by.This field is null when the system does not expect the report to receive abounty at this time. |
| » timer_bounty_awarded_elapsed_time | integer¦null | false | The total number of seconds that have elapsed between when the timer startedand when it stopped ticking. The timer does not take weekends into account.If this field is null and the corresponding`miss_at` field is set, it meansthe timer is still counting. |
| » timer_first_program_response_miss_at | date-time¦null | false | The date and time the system expects the program to have posted an initialpublic comment to the report by. |
| » timer_first_program_response_elapsed_time | integer¦null | false | The total number of seconds that have elapsed between when the timer startedand when it stopped ticking. The timer does not take weekends into account.If this field is null and the corresponding`miss_at` field is set, it meansthe timer is still counting. |
| » timer_report_resolved_miss_at | date-time¦null | false | The date and time the system expects the program to have closed the report by.This field is null when the report seems blocked by the reporter. |
| » timer_report_resolved_elapsed_time | integer¦null | false | The total number of seconds that have elapsed between when the timer startedand when it stopped ticking. The timer does not take weekends into account.If this field is null and the corresponding`miss_at` field is set, it meansthe timer is still counting. |
| » timer_report_triage_miss_at | date-time¦null | false | The date and time the system expects the program to have triaged the report by.This field is null when the system does not expect the report to be triaged atthis time. |
| » timer_report_triage_elapsed_time | integer¦null | false | The total number of seconds that have elapsed between when the timer startedand when it stopped ticking. The timer does not take weekends into account.If this field is null and the corresponding`miss_at` field is set, it meansthe timer is still counting. |
| » original_report_id | string¦null | false | Id of the report this report has been cloned from. |
| » hai_is_priority | boolean¦null | false | Indicates whether the report has been flagged as high priority based onPrioritization Agent analysis. This field is only populated for reports withpriority recommendation data and on Enterprise product editions |
| » hai_is_priority_reason | string¦null | false | A short explanation of why the report was flagged as priority. This fieldis only present when`hai_is_priority` is true. |
| relationships | object | true | none |
| » program | object | true | The program that received the report. |
| »» data | [program_small](https://api.hackerone.com/customer-reference#program_small) | true | A program object represents a disclosure program or bug bounty program on theplatform. When [a user](https://api.hackerone.com/customer-reference#user) reports a bug to a program, this isthe object they interact with. Behind a program, there can be multiple usersthat are part of the program. Those users can interact with reports on behalfof the program. |
| » assignee | object | false | The user or group that is assigned to handle the report. |
| »» data | any | false | none |

oneOf - discriminator: user.type

Last revised: 2026-04-14

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| »»» anonymous | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

xor - discriminator: group.type

Last revised: 2026-04-14

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| »»» anonymous | [group](https://api.hackerone.com/customer-reference#group) | false | A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports. |

continued

Last revised: 2026-04-14

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| » attachments | object | false | A list of Attachment objects that the reporter added to the report. |
| »» data | [[attachment](https://api.hackerone.com/customer-reference#attachment)] | false | [Users can add attachments when they file a report or when they interact with areport. Attachments may contain dangerous proof of concepts and should be handledwith caution.] |
| » swag | object | false | A list of Swag objects that were awarded to the reporter. |
| »» data | [[swag](https://api.hackerone.com/customer-reference#swag)] | false | [Besides a financial reward, which is called [a bounty](https://api.hackerone.com/customer-reference#bounty), programs canaward swag. Report objects may contain multiple swag objects, one for each timeswag was awarded.] |
| » weakness | object | false | The Weakness object of the report provided by the reporter or team. |
| »» data | [weakness](https://api.hackerone.com/customer-reference#weakness) | false | A Weakness object represents the type of weakness the hacker submitted to a program.The weakness was initially provided by the hacker, but may be reviewed and correctedby the program. |
| » structured_scope | object | false | The StructuredScope object of the report provided by the reporter or team. |
| »» data | [structured-scope](https://api.hackerone.com/customer-reference#structured-scope) | false | A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program. |
| » campaign | object¦null | false | The Campaign associated with the report, if any. |
| »» data | [campaign](https://api.hackerone.com/customer-reference#campaign) | false | A campaign object represents a bounty campaign for a program. Campaigns allowprogram managers to incentivize hackers by offering bounty multipliers onspecific assets for a limited time. |
| » severity | object | false | The Severity object of the report provided by the reporter or team. |
| »» data | [severity](https://api.hackerone.com/customer-reference#severity) | false | A severity object represents the severity of a report, if provided by the reporter ora team member. |
| » reporter | object | false | The user that created the report. This object contains the user's reputation, signal,and impact metrics. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |
| » triggered_pre_submission_trigger | object | false | A pre-submission trigger that notified the hacker before submission.This field is only present for reports filed after February 14, 2016. |
| »» data | [trigger](https://api.hackerone.com/customer-reference#trigger) | false | Triggers are a way to show a pop-up message or to automatically reply to reportsbased on their title or content. |
| » activities | object | false | A list of Activity objects that can be used to generate a timeline of changes.Activities are ordered by most recent first. |
| »» data | [[activity](https://api.hackerone.com/customer-reference#activity)] | false | [These objects represent an action that was performed on a [report](https://api.hackerone.com/customer-reference#report) or on a [program](https://api.hackerone.com/customer-reference#program).Activities come in many sub types that can have additional attributes.] |
| » bounties | object | false | A list of Bounty objects that were awarded to the reporter. |
| »» data | [[bounty](https://api.hackerone.com/customer-reference#bounty)] | false | [When a program pays a bounty to the hacker, a bounty object is created.A report may contain multiple bounty objects, one for each time a bounty wasawarded. The hacker that reported the vulnerability is the user that receivedthe bounty.] |
| » summaries | object | false | A list of Report Summary objects that were added to the report by the reporterand team. |
| »» data | [[report-summary](https://api.hackerone.com/customer-reference#report-summary)] | false | [Before a report is disclosed, the program, the HackerOne Triage team and hacker may add a summary. Areport can have only one summary per party. Unlike activities, summaries canbe edited through HackerOne indefinitely. Triage summaries are onlyvisible to team members and the HackerOne Triage team.] |
| » custom_field_values | object | false | A list of Custom Field Value objects containing all Custom Field Attributesthat are set for the report. Enterprise only. |
| »» data | [[custom-field-value](https://api.hackerone.com/customer-reference#custom-field-value)] | false | [A Custom Field Value object contains the value set for a particularCustom Field Attribute.] |
| » automated_remediation_guidance | object | false | Remediation guidance that has been derived from the report's weakness. |
| »» data | [automated-remediation-guidance](https://api.hackerone.com/customer-reference#automated-remediation-guidance) | false | Remediation guidance that has been derived from the report's weakness. |
| » custom_remediation_guidance | object | false | Custom remediation guidance that has been written by a team member. |
| »» data | [custom-remediation-guidance](https://api.hackerone.com/customer-reference#custom-remediation-guidance) | false | Custom remediation guidance that has been written by a team member. |
| » inboxes | object | false | A list of inboxes the report appears in. |
| »» data | [[inbox](https://api.hackerone.com/customer-reference#inbox)] | false | [An inbox object represents an inbox that belongs to an organization and holds a set of reports.Default (aka program inboxes) are created by the system and cannot be deleted and hold all reports of the programCustom inboxes are created by the user and can be deleted and hold only reports that are explicitly assigned to them.] |

Enumerated Values

| Property | Value |
| --- | --- |
| type | report |

## report-main-states

```
"draft"

```

Last revised: 2022-09-15

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| report-main-states | string | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| report-main-states | draft |
| report-main-states | open |
| report-main-states | closed |

## report-states

```
"new"

```

Last revised: 2021-06-25

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| report-states | string | false | none |

Enumerated Values

| Property | Value |
| --- | --- |
| report-states | new |
| report-states | pending-program-review |
| report-states | triaged |
| report-states | needs-more-info |
| report-states | resolved |
| report-states | not-applicable |
| report-states | informative |
| report-states | duplicate |
| report-states | spam |
| report-states | retesting |

## report-summary

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

Last revised: 2021-06-25

Before a report is disclosed, the program, the HackerOne Triage team and hacker may add a summary. A report can have only one summary per party. Unlike activities, summaries can be edited through HackerOne indefinitely. Triage summaries are only visible to team members and the HackerOne Triage team.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the report summary. |
| type | string | true | none |
| attributes | object | true | none |
| » content | string | true | The raw summary of the report. Markdown is not parsed. |
| » category | string | true | The involved party that wrote the summary. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was last updated. Formatted accordingto ISO 8601. |
| relationships | object | true | none |
| » user | object | true | The author that added the summary to the report. |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | report-summary |
| category | researcher |
| category | team |
| category | triage |

## scope-exclusion

```
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

```

Last revised: 2026-04-16

A scope exclusion object represents a report category that is excluded from rewards for a program, in addition to the core ineligible findings.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the scope exclusion. |
| type | string | true | none |
| attributes | object | true | none |
| » category | string¦null | false | The category name for the scope exclusion. |
| » details | string¦null | false | Description of what is excluded from the program scope. |
| » created_at | string(date-time) | false | The date and time the object was created. Formatted according to ISO 8601. |
| » updated_at | string(date-time) | false | The date and time the object was updated. Formatted according to ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | scope-exclusion |

## severity

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

Last revised: 2025-01-22

A severity object represents the severity of a report, if provided by the reporter or a team member.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the severity. |
| type | string | true | none |
| attributes | object | true | none |
| » rating | [severity-ratings](https://api.hackerone.com/customer-reference#severity-ratings) | true | The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score. |
| » author_type | string | true | The involved party that provided the severity. |
| » user_id | integer | true | The unique id of the user who created the object. |
| » score | number¦null | false | The vulnerability score calculated from the Common Vulnerability Scoring System (CVSS).Only present if CVSS metrics were provided. |
| » attack_vector | string¦null | false | A CVSS metric that reflects the context by which vulnerability exploritationis possible. |
| » attack_complexity | string | false | A CVSS metric that describes the conditions beyond the attacker's control that must existin order to exploit the vulnerability. |
| » privileges_required | string | false | A CVSS metric that describes the level of privileges an attacker must possess beforesuccessfully exploiting the vulnerability. |
| » user_interaction | string | false | A CVSS metric that captures the requirement for a user, other than the attacker, toparticipate in the successful compromise of the vulnerability component. |
| » scope | string¦null | false | A CVSS metric that determines if a successful attack impacts a component other than thevulnerable component. |
| » confidentiality | string | false | A CVSS metric that measures the impact to the confidentiality of the information resourcesmanaged by a software component due to a successfully exploited vulnerability. |
| » integrity | string | false | A CVSS metric that measures the impact to the integrity of a successfully exploitedvulnerability. |
| » availability | string | false | A CVSS metric that measures the availability of the impacted component resulting from asuccessfully exploited vulnerability. |
| » calculation_method | string | false | The method used to calculate the severity. If the severity was manually set by anemployee, the value will be`manual`. If the severity was calculated by HackerOne'sCVSS 3.0 calculator, the value will be`cvss_3_0_hackerone`. If the severity wascalculated by the official CVSS 3.1 calculator, the value will be`cvss_3_1`. |
| » cvss_vector_string | string | false | If severity method is not manual, there will be a CVSS vector string. This is a string that is generated based on the given environmental scores. |
| » message | string | false | Optional reason for the severity value. |
| » cvss_4_0_metric_set | object | false | A set of CVSS 4.0 metrics that describe the severity of a vulnerability.Only available if the severity was calculated using CVSS 4.0. |
| »» attack_vector | string | false | A CVSS metric that reflects the context by which vulnerability exploritationis possible. |
| »» attack_complexity | string | false | A CVSS metric that describes the conditions beyond the attacker's control that must existin order to exploit the vulnerability. |
| »» attack_requirements | string | false | A CVSS metric that captures the prerequisite deployment and execution conditions or variablesof the vulnerable system that enable the attack. |
| »» privileges_required | string | false | A CVSS metric that describes the level of privileges an attacker must possess beforesuccessfully exploiting the vulnerability. |
| »» user_interaction | string | false | A CVSS metric that captures the requirement for a user, other than the attacker, toparticipate in the successful compromise of the vulnerability component. |
| »» vulnerable_confidentiality | string | false | A CVSS metric that measures the impact to the confidentiality of the information resourcesmanaged by a software component due to a successfully exploited vulnerability. |
| »» vulnerable_integrity | string | false | This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity refers to the trustworthiness and veracity of information. |
| »» vulnerable_availability | string | false | This metric measures the impact to the availability of the impacted system resulting from a successfully exploited vulnerability. |
| »» subsequent_confidentiality | string | false | This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability of subsequent systems. |
| »» subsequent_integrity | string | false | This metric measures the impact to integrity of a successfully exploited vulnerability of subsequent systems. Integrity refers to the trustworthiness and veracity of information. |
| »» subsequent_availability | string | false | This metric measures the impact to the availability of the impacted system resulting from a successfully exploited vulnerability of subsequent systems. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | severity |
| author_type | User |
| author_type | Team |
| attack_vector | network |
| attack_vector | adjacent |
| attack_vector | local |
| attack_vector | physical |
| attack_complexity | low |
| attack_complexity | high |
| privileges_required | none |
| privileges_required | low |
| privileges_required | high |
| user_interaction | none |
| user_interaction | required |
| scope | unchanged |
| scope | changed |
| confidentiality | none |
| confidentiality | low |
| confidentiality | high |
| integrity | none |
| integrity | low |
| integrity | high |
| availability | none |
| availability | low |
| availability | high |
| calculation_method | manual |
| calculation_method | cvss_3_0_hackerone |
| calculation_method | cvss_3_1 |
| attack_vector | network |
| attack_vector | adjacent |
| attack_vector | local |
| attack_vector | physical |
| attack_complexity | low |
| attack_complexity | high |
| attack_requirements | none |
| attack_requirements | present |
| privileges_required | none |
| privileges_required | low |
| privileges_required | high |
| user_interaction | none |
| user_interaction | required |
| vulnerable_confidentiality | none |
| vulnerable_confidentiality | low |
| vulnerable_confidentiality | high |
| vulnerable_integrity | none |
| vulnerable_integrity | low |
| vulnerable_integrity | high |
| vulnerable_availability | none |
| vulnerable_availability | low |
| vulnerable_availability | high |
| subsequent_confidentiality | none |
| subsequent_confidentiality | low |
| subsequent_confidentiality | high |
| subsequent_integrity | none |
| subsequent_integrity | low |
| subsequent_integrity | high |
| subsequent_availability | none |
| subsequent_availability | low |
| subsequent_availability | high |

## severity-ratings

```
"none"

```

Last revised: 2021-06-25

The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| severity-ratings | string | false | The qualitative rating of the severity. Provided either directly from the author or mapped from the calculated vulnerability score. |

Enumerated Values

| Property | Value |
| --- | --- |
| severity-ratings | none |
| severity-ratings | low |
| severity-ratings | medium |
| severity-ratings | high |
| severity-ratings | critical |

## structured-scope

```
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
}

```

Last revised: 2025-06-10

A StructuredScope object represents an asset defined by the program. The scope on a report was initially provided by the hacker, but may be reviewed and corrected by the program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the scope. |
| type | string | true | none |
| attributes | object | true | none |
| » asset_identifier | string | true | The identifier of the asset. |
| » asset_type | string | true | The type of the asset. |
| » eligible_for_bounty | boolean | true | If the asset is eligible for bounty. |
| » eligible_for_submission | boolean | true | If the asset is eligible for submission. |
| » instruction | string¦null | false | The raw intruction of the asset provided by the program.Markdown is not parsed. |
| » confidentiality_requirement | string | false | A CVSS environmental modifier that reweights Confidentiality Impactof a vulnerability on this asset. |
| » integrity_requirement | string | false | A CVSS environmental modifier that reweights Integrity Impact of avulnerability on this asset. |
| » availability_requirement | string | false | A CVSS environmental modifier that reweights Availability Impact ofa vulnerability on this asset. |
| » max_severity | string | true | The qualitative rating of the maximum severity allowed on this asset. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |
| » updated_at | string(date-time) | true | The date and time the object was updated. Formatted according to ISO 8601. |
| » reference | string¦null | false | The customer defined reference identifier or tag of the asset. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | structured-scope |
| confidentiality_requirement | none |
| confidentiality_requirement | low |
| confidentiality_requirement | medium |
| confidentiality_requirement | high |
| integrity_requirement | none |
| integrity_requirement | low |
| integrity_requirement | medium |
| integrity_requirement | high |
| availability_requirement | none |
| availability_requirement | low |
| availability_requirement | medium |
| availability_requirement | high |
| max_severity | none |
| max_severity | low |
| max_severity | medium |
| max_severity | high |
| max_severity | critical |

## swag

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

Last revised: 2025-06-10

Besides a financial reward, which is called [a bounty](https://api.hackerone.com/customer-reference#bounty), programs can award swag. Report objects may contain multiple swag objects, one for each time swag was awarded.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the swag. |
| type | string | true | none |
| attributes | object | true | none |
| » sent | boolean | true | Indicates whether the swag has been marked as sent. Swag can be marked assent through the HackerOne interface. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » user | object | true | none |
| »» data | [user](https://api.hackerone.com/customer-reference#user) | true | The user the swag was awarded to. |
| » address | object | true | none |
| »» data | [address](https://api.hackerone.com/customer-reference#address) | true | The user's address to send the swag to. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | swag |

## team_message

```
{
  "id": "12345",
  "type": "team-message",
  "attributes": {
    "state": "sent",
    "created_at": "2025-06-15T14:30:45Z"
  }
}

```

Last revised: 2025-07-21

When a program sends a message to hackers, a team_message object is created. Messages can be sent to various groups of hackers based on their participation in the program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the team message. |
| type | string | true | none |
| attributes | object | true | none |
| » state | string | false | The current state of the message. |
| » created_at | string(date-time) | false | The date and time the message was created. Formatted accordingto ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | team-message |
| state | sent |
| state | invalid |
| state | needs-action |
| state | needs-review |

## thanks-item

```
{
  "type": "thanks-item",
  "attributes": {
    "total_report_count": 1,
    "reputation": 7,
    "recognized_report_count": 1,
    "username": "lorem",
    "user_id": "55"
  }
}

```

Last revised: 2024-02-08

A thanks item object represents thanks given to hackers by program members

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| attributes | object | true | none |
| » total_report_count | integer | true | The number of reports |
| » reputation | integer | true | The reputation of the user |
| » recognized_report_count | integer | true | The number of resolved reports |
| » username | string | true | The username of the user |
| » user_id | string | true | The ID of the user |

## transaction

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

Last revised: 2025-06-10

A Transaction object represents the information about the program payment transaction.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The unique ID of the transaction. |
| type | string | true | none |
| attributes | object | true | none |
| » activity_date | string(date-time) | true | The date and time of the activity. Formatted accordingto ISO 8601. |
| » activity_description | string | true | The description of the activity. |
| » balance | string | true | The date of the payment. |
| » bounty_award | string¦null | true | The amount of awarded bounty. |
| » bounty_fee | string¦null | true | The HackerOne bounty fee. |
| » debit_or_credit_amount | string | false | The amount that's debited or credited from your balance. |
| relationships | object | false | none |
| » report | object | false | none |
| »» data | object | true | none |
| »»» id | integer | true | The ID of the report with the awarded bounty. |
| »»» type | string | true | none |
| »» links | object | true | none |
| »»» self | string | true | The URL of the report with the awarded bounty. |
| » user | object | false | none |
| »» data | object | true | none |
| »»» id | integer | true | The ID of the hacker awarded with the bounty. |
| »»» type | string | true | none |
| »» attributes | object | false | none |
| »»» username | string | false | The username of the hacker awarded with the bounty. |
| »» links | object | true | none |
| »»» self | string | true | The URL to the hacker awarded with the bounty. |
| » payer | object | false | none |
| »» data | object | true | none |
| »»» id | integer | true | The ID of the user paying the bounty. |
| »»» type | string | true | none |
| »» attributes | object | true | none |
| »»» username | string | false | The username of the user paying the bounty. |
| »» links | object | true | none |
| »»» self | string | true | The URL to the user paying the bounty. |
| » team | object | false | none |
| »» data | object | true | none |
| »»» id | integer | true | The ID of the team handling the bounty. |
| »»» type | string | true | none |
| »» attributes | object | false | none |
| »»» handle | string | false | The nickname of the team handling the bounty. |
| »» links | object | true | none |
| »»» self | string | true | The URL to the team handling the bounty. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | payment-transaction |
| type | report |
| type | user |
| type | user |
| type | team |

## triage-review

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

Last revised: 2024-11-19

A Triage Review object represents a rating and feedback for a specific report.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique identifier for the triage review. |
| type | string | true | The type of the resource. |
| attributes | object | true | none |
| » comment | string | false | Feedback comment for the rating. |
| » rating | integer | false | Numeric value representing the rating score. |
| relationships | object | true | none |
| » user | object | false | none |
| »» data | object | false | none |
| »»» id | string | true | The unique identifier for the user. |
| »»» type | string | true | The type of the related resource. |
| »»» attributes | object | true | none |
| »»»» username | string | true | Username of the user associated with the rating. |
| » report | object | false | none |
| »» data | object | false | none |
| »»» id | string | true | The unique identifier for the report. |
| »»» type | string | true | The type of the related resource. |
| »»» attributes | object | true | none |
| »»»» title | string | true | Title of the report associated with the rating. |

## trigger

```
{
  "id": "1337",
  "type": "trigger",
  "attributes": {
    "title": "Example Trigger"
  }
}

```

Last revised: 2024-02-08

Triggers are a way to show a pop-up message or to automatically reply to reports based on their title or content.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the trigger. |
| type | string | true | none |
| attributes | object | true | none |
| » title | string¦null | false | The name of the trigger. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | trigger |

## user

```
{
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
    "user_type": "hacker"
  }
}

```

Last revised: 2025-10-16

User objects represent accounts on HackerOne. These objects are mostly referenced when someone performed an action using that account. All different actors on the platform, hackers, API users, and program users, have a user account.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the user. |
| type | string | true | none |
| attributes | object | true | none |
| » disabled | boolean | true | Indicates if the user is disabled. |
| » username | string | true | The username of the user. Usernames are unique and scoped under the samenamespace as program handles. |
| » name | string | true | The name of the user. A name may be empty and is free-format. |
| » profile_picture | object | true | An object that holds URLs to different profile picture sizes. |
| »» 62x62 | string | true | none |
| »» 82x82 | string | true | none |
| »» 110x110 | string | true | none |
| »» 260x260 | string | true | none |
| » bio | string¦null | false | The user's biography, as provided by the user. |
| » website | string¦null | false | The user's website, as provided by the user. |
| » location | string¦null | false | The user's location, as provided by the user. |
| » reputation | number¦null | false | The reputation of the user. Read more about how this number iscalculated [here](https://www.hackerone.com/blog/introducing-reputation). Thisattribute is only included in the reporter relationship of areport object. |
| » signal | number¦null | false | The signal of the user. This number ranges from -10 to 7. The closer to 7,the higher the average submission quality of the user. This attribute is onlyincluded in the reporter relationship of a report object.Learn more about how this number is calculated [here](https://www.hackerone.com/blog/introducing-signal-and-impact). |
| » impact | number¦null | false | The impact of the user. This number ranges from 0 to 50. The closer to 50,the higher the average severity of the user's reports is. This attribute is onlyincluded in the reporter relationship of a report object.Learn more about how this number is calculated [here](https://www.hackerone.com/blog/introducing-signal-and-impact). |
| » hackerone_triager | boolean¦null | false | Indicates if the user is a hackerone triager. |
| » user_type | string¦null | false | The type of user account. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted accordingto ISO 8601. |
| relationships | object | false | none |
| » participating_programs | object | false | none |
| »» data | [object] | false | List of private programs that you manage where this user is invited to.This attribute is only included when making use of the User > Read endpoint. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | user |

## weakness

```
{
  "id": "1337",
  "type": "weakness",
  "attributes": {
    "name": "Cross-Site Request Forgery (CSRF)",
    "description": "The web application does not, or can not, sufficiently verify whether a well-formed, valid, consistent request was intentionally provided by the user who submitted the request.",
    "created_at": "2016-02-02T04:05:06.000Z",
    "external_id": "cwe-352"
  }
}

```

Last revised: 2024-02-08

A Weakness object represents the type of weakness the hacker submitted to a program. The weakness was initially provided by the hacker, but may be reviewed and corrected by the program.

Attributes

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | true | The unique ID of the weakness. |
| type | string | true | none |
| attributes | object | true | none |
| » name | string | true | The name of the weakness. |
| » description | string | true | The raw description of the weakness. Markdown is not parsed. |
| » external_id | string | true | The weakness' external reference to CWE or CAPEC. |
| » created_at | string(date-time) | true | The date and time the object was created. Formatted according to ISO 8601. |

Enumerated Values

| Property | Value |
| --- | --- |
| type | weakness |