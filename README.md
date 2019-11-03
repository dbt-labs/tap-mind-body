# tap-mind-body

Author: Jacob Werderits (jacob@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:
- Generates a catalog of available data in MindBody using the V6.0 Public Api
- Extracts the following resources:
  - [Classes](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-classes)
  - [ClassDescriptions](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-class-descriptions)
  - [ClassSchedules](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-class-schedules)
  - [ClassVisits](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-class-visit)
  - [WaitListEntries](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-wait-list-entries)
  - [Clients](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-clients)
  - [ClientPurchases](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-client-purchases)
  - [Sales](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-sales)
  - [AcceptedCardTypes](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-accepted-card-types)
  - [Contracts](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-contracts)
  - [CustomPaymentMethods](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-custom-payment-methods)
  - [GiftCards](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-gift-cards)
  - [Packages](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-packages)
  - [Products](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-products)
  - [Services](https://developers.mindbodyonline.com/PublicDocumentation/V6?python#get-services)
  
## Quick Start

### 1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-mind-body.git
cd tap-mind-body
pip install .
```

### 2. Accessing Data from Mindbody

To develop and integrate an application using the MINDBODY [Public API](https://developers.mindbodyonline.com/PublicDocumentation/V6#mindbody-public-api-v6-0), you’ll need to do the following:

1. Create a MINDBODY developer account.
2. Write your application, using the MINDBODY sandbox for development and testing.
3. Request approval from MINDBODY to take your application live.
4. Request a site-specific activation code or an activation link for a specific business owner’s MINDBODY account so that your application can access the owner’s business data.
5. Send the activation code or the activation link to the business owner to activate.
You’ll need to follow these processes in the order given.



### 3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your tokens.
To get the Authorization token, you can use the [issue](https://developers.mindbodyonline.com/PublicDocumentation/V6#user-tokens) endpoint to pass User Credentials.

**Note:** For all endpoints, user credentials may alter the returned data based on the creator of the passed token.


### 4. Run the application to generate a catalog.

```bash
tap-mind-body -c config.json --discover > catalog.json
```

### 5. Select the tables you'd like to replicate

Step 4 generates a a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

### 6. Run it!

```bash
tap-mind-body -c config.json --catalog catalog.json
```

Copyright &copy; 2019 Fishtown Analytics
