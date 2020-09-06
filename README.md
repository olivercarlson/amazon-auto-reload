## TODOS:

-   1. Add basic pre-run checking for typos on all credit card information (no whitespace, length = 16, etc.) and throw errors if any are found.

-   2. After script runs, use chalk to display outputs of the reloads to the user.

-   3. Add remove card functionality option, which will consist of (1) adding flag to whitelist credit card numbers and then (2) remove all non-whitelisted credit card numbers.

-   4. if more occur: Continue debugging errors after changes to Amazon website.

-   5. (low priority) Investigate OS X issue with pathing to Chrome browser not working. Instead, will likely move to investigate docker build issues afterwards as thats a superior solution for removing compatability issues that could be OS dependent.

## History:

9/6/20:

-   Appears the issue "Investigate Unhandled promise rejection error after finishing up a card yesterday (failed at amazon.ts line #156)" does not occur consistently. May have been the result of a typo not fixed before compiling tsc again.

8/25/20:

-   Added tsc-watch package and "npm run dev" command to the package.json to automatically rebuild TS code and run after completion.
-   Changed the xpath command to find again find the correct DOM Node - now uses the "data-number" to find the last 4 digits and click. As a result, the program works again on Firefox x64 79.0.0 && OS X 10.15.6.

8/24/20:

-   Initial fork and set up of repository. Added tnortman's PR changes to update DOM tree navigation based off of current changes.
-   Added updates from pull request not yet merged to original branch by @tnortman.
-   Changed Firefox to default browser. (due to unresolved pathing error with chrome on OSX)

## Forked everettsouthwick/amazon-auto-reload

![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightscreen.svg)

This script automates the process of reloading Amazon gift card balances with configurable amounts and transactions per execution. This is useful to maximize credit and/or debit card rewards or to prevent the closure of a credit card account due to inactivity.

## Dependencies

-   [Node.js](https://nodejs.org/)
-   Chrome or Firefox desktop browser installed

## Getting Started

1. Clone or download the project
2. Copy [`config/default-example.json5`](config/default-example.json5) to `config/default.json5` and modify it with your details
3. Execute `npm install && npm run build && npm start`

## Features

-   Allows you to use Chrome and Firefox
-   Browser is visible to provide peace of mind as to what is happening
-   Configurable/extensible

## Docker

Includes a Docker configuration. To utilize:

1. Execute `npm run docker:build && npm run docker:run`
2. You then need to VNC into port 5900, open a shell, and execute `npm start`

Ideally we would start our app as soon as we run our Docker image, removing the need for step 2, but haven't yet been able to make it work - the desktop browsers error out when instantiated. Perhaps they're being instantiated before the desktop interface within the Docker container is ready?

## TODO

-   Add tests
-   Try for a more attractive code approach to the code's many webdriver action calls
-   Create a scheduler

## Acknowledgements

Browser / Site class model inspired by [typescript-selenium-example](/goenning/typescript-selenium-example)

## Similar

[amazon-reload-balance](https://github.com/rhobot/amazon-reload-balance)

## Rewrite history

A rewritten version of this app using Typescript was released in 2019-05. A rewritten version of this app using Node.js was released on 2019-04-01. To find the original python version, see the branch [`deprecated-python`](../../tree/deprecated-python). The Python version won't receive further updates/support.
