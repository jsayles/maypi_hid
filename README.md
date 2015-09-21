# The MayPi Doorman System
The MayPi Doorman System was developed to serve as the electronic doorman at the newly renovated
Red Victorian Coliving Hotel in San Francisco's historic Haight Ashbury neighborhood.

This implementation works with the HID Edge Solo door controllers.

## What's in a name?
MayPi is named after William May.  William May has been The Fairmont San Francisco's Doorman for over 27 years! As he likes to say this service has helped him earn his PhD in People. He's now up for a Hotel Hero Award for Lifetime Achievement in Operations. 
Learn more here: 
 - https://www.youtube.com/watch?v=c4ozJKBp0XI

## Components

### Gatekeeper
The Gatekeeper controlls the door controllers.  This runs on a computer (raspberry pi for example) on the same private network as the doors.  This is designed to not have a database or anything written to disk so that the pi can be booted readonly.

### Keymaster
The Keymaster has all the keys.  The member management communicates with the Keymaster and the Gatekeeper requests the keys from the Keymaster.