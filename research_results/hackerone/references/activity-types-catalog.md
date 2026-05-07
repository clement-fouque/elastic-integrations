# HackerOne Customer API — Activity type catalog

Source: [Customer Reference — activity](https://api.hackerone.com/customer-reference#activity) and per-type subsections (`activity-*`).

Each activity **inherits** the base [`activity`](https://api.hackerone.com/customer-reference#activity) schema (attributes: `id`, `type`, `report_id`, `message`, `internal`, `created_at`, `updated_at`; relationships: `actor` (user or program), `attachments`). Type-specific fields and relationships are documented under each heading below.

**Total activity types:** 63

## `activity-agreed-on-going-public`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» disclosed_at | string(date-time)¦null | false | none |
| »» allow_singular_disclosure_at | string(date-time)¦null | false | none |

---

## `activity-bounty-awarded`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» bounty_amount | string | false | none |
| »» bonus_amount | string | false | none |

---

## `activity-bounty-suggested`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» bounty_amount | string | false | none |
| »» bonus_amount | string | false | none |

---

## `activity-bug-cloned`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» original_report_id | integer | true | none |

---

## `activity-bug-duplicate`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» original_report_id | integer | false | none |

---

## `activity-bug-filed`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-inactive`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-informative`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-needs-more-info`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-new`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-not-applicable`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-priority-changed`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» priority | string¦null | false | none |

---

## `activity-bug-reopened`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-resolved`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-retesting`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-spam`

**Example (from customer-reference):**

```json
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

---

## `activity-bug-triaged`

**Example (from customer-reference):**

```json
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

---

## `activity-cancelled-disclosure-request`

**Example (from customer-reference):**

```json
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

---

## `activity-changed-scope`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» old_scope | object | true | none |
| »»» data | [structured-scope](https://api.hackerone.com/customer-reference#structured-scope) | false | A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program. |
| »» new_scope | object | true | none |
| »»» data | [structured-scope](https://api.hackerone.com/customer-reference#structured-scope) | false | A StructuredScope object represents an asset defined by the program. The scope on areport was initially provided by the hacker, but may be reviewed and corrected bythe program. |

---

## `activity-comment`

**Example (from customer-reference):**

```json
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

---

## `activity-comments-closed`

**Example (from customer-reference):**

```json
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

---

## `activity-draft-started`

**Example (from customer-reference):**

```json
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

---

## `activity-external-user-invitation-cancelled`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» email | string¦null | false | none |

---

## `activity-external-user-invited`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» email | string¦null | false | none |

---

## `activity-external-user-joined`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» duplicate_report_id | integer | false | none |

---

## `activity-external-user-removed`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» removed_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

---

## `activity-group-assigned-to-bug`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» group | object | true | none |
| »»» data | [group](https://api.hackerone.com/customer-reference#group) | false | A group represents a set of users. A group is used to delegate permissions forthe users in it. It can also be assigned to one or multiple reports. |

---

## `activity-hacker-requested-mediation`

**Example (from customer-reference):**

```json
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

---

## `activity-invitation-received`

**Example (from customer-reference):**

```json
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

---

## `activity-manually-disclosed`

**Example (from customer-reference):**

```json
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

---

## `activity-mediation-requested`

**Example (from customer-reference):**

```json
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

---

## `activity-nobody-assigned-to-bug`

**Example (from customer-reference):**

```json
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

---

## `activity-not-eligible-for-bounty`

**Example (from customer-reference):**

```json
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

---

## `activity-program-hacker-joined`

**Example (from customer-reference):**

```json
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

---

## `activity-program-hacker-left`

**Example (from customer-reference):**

```json
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

---

## `activity-program-inactive`

**Example (from customer-reference):**

```json
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

---

## `activity-reassigned-to-team`

**Example (from customer-reference):**

```json
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

---

## `activity-recommendation-created`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» recommended_action | string¦null | false | none |

---

## `activity-reference-id-added`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» reference | string | true | none |
| »» reference_url | string | true | none |

---

## `activity-report-became-public`

**Example (from customer-reference):**

```json
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

---

## `activity-report-collaborator-invited`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» email | string¦null | false | none |

---

## `activity-report-collaborator-joined`

**Example (from customer-reference):**

```json
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

---

## `activity-report-custom-field-value-updated`

**Example (from customer-reference):**

```json
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

---

## `activity-report-prioritised`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» high_priority | boolean | true | none |
| »» high_priority_reason | string¦null | false | none |

---

## `activity-report-remediation-guidance-updated`

**Example (from customer-reference):**

```json
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

---

## `activity-report-retest-approved`

**Example (from customer-reference):**

```json
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

---

## `activity-report-retest-rejected`

**Example (from customer-reference):**

```json
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

---

## `activity-report-severity-updated`

**Example (from customer-reference):**

```json
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

---

## `activity-report-title-updated`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» old_title | string | true | none |
| »» new_title | string | true | none |

---

## `activity-report-triage-summary-created`

**Example (from customer-reference):**

```json
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

---

## `activity-report-triage-summary-updated`

**Example (from customer-reference):**

```json
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

---

## `activity-report-vulnerability-information-updated`

**Example (from customer-reference):**

```json
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

---

## `activity-report-vulnerability-types-updated`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» old_weakness | object | false | The weakness that was set before the change |
| »»» data | [weakness](https://api.hackerone.com/customer-reference#weakness) | false | A Weakness object represents the type of weakness the hacker submitted to a program.The weakness was initially provided by the hacker, but may be reviewed and correctedby the program. |
| »» new_weakness | object | false | The weakness that was set after the change |
| »»» data | [weakness](https://api.hackerone.com/customer-reference#weakness) | false | A Weakness object represents the type of weakness the hacker submitted to a program.The weakness was initially provided by the hacker, but may be reviewed and correctedby the program. |

---

## `activity-retest-user-expired`

**Example (from customer-reference):**

```json
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

---

## `activity-swag-awarded`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» swag | object | true | none |
| »»» data | [swag](https://api.hackerone.com/customer-reference#swag) | false | Besides a financial reward, which is called [a bounty](https://api.hackerone.com/customer-reference#bounty), programs canaward swag. Report objects may contain multiple swag objects, one for each timeswag was awarded. |

---

## `activity-triage-intake-completed`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» reference | string | false | none |
| »» reference_url | string | false | none |

---

## `activity-triage-intake-exited`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| »» intake_outcome | string¦null | false | none |
| »» abort_reason | string¦null | false | none |
| »» va_suggestion | string¦null | false | none |
| »» report_state_change | string¦null | false | none |

---

## `activity-user-assigned-to-bug`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» assigned_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

---

## `activity-user-banned-from-program`

**Example (from customer-reference):**

```json
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

**Type-specific schema rows (supplemental `allOf` tables):**

| Path | Type | Required | Description |
| --- | --- | --- | --- |
| » relationships | object | false | none |
| » relationships | object | false | none |
| »» removed_user | object | true | none |
| »»» data | [user](https://api.hackerone.com/customer-reference#user) | false | User objects represent accounts on HackerOne. These objects are mostly referencedwhen someone performed an action using that account. All different actors on theplatform, hackers, API users, and program users, have a user account. |

---

## `activity-user-completed-retest`

**Example (from customer-reference):**

```json
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

---

## `activity-user-left-retest`

**Example (from customer-reference):**

```json
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

---

## `activity-validation-recommendation-accepted`

**Example (from customer-reference):**

```json
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

---

## `activity-validation-recommendation-rejected`

**Example (from customer-reference):**

```json
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

---
