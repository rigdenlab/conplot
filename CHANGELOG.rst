Changelog
=========


0.2.4
-----

Added
~~~~~
- Fixed minor bugs (issues #101, #104 and #106)
- Added references to web-app hosting by CCP4-online
- Updated help page and tutorials to match latest version

Changed
~~~~~~~
- Figure and display settings are now stored in the cache


0.2.3
-----

Added
~~~~~
- Ensure user reads GDPR before creating account
- Created tutorial about ab initio model validation by superimposing contact maps
- Handle database conection errors


Changed
~~~~~~~
- Moved all docker related files to a separate repository
- Migrate cache to KeyDB
- Several improvements to UI based on user feedback
- Bug fix: handle exceptions when uploading binary files
- Bug fix: superimposing a contact prediction with a PDB file shows all contacts in the PDB model indepdently of L/ filter
- Implement PDB parser based on biopython. Only reads first chain for performance.


0.2.2
-----

Added
~~~~~
- Changed ROOT to /conplot for deployment


0.2.1
-----

Added
~~~~~
- Enabled deployment with docker containers


0.2
----

Added
~~~~~

- Superimpose contact maps: if more than one contact map is uploaded users can choose to superimpose them
- Control over half squares of the contact map: users can select which data to display on each half of the map
- Transparent tracks switch: users can choose if they want transparent tracks or not
- Help page contents have been created: tutorials, layout information...etc.
- Multiple colour palettes are available for each track
- Added GDPR privacy policy banner


Changed
~~~~~~~
- Upload multiple files per track: users can now upload more than one file for each dataset type
- Changed contents on home and rigden lab pages
- Updated layout of navigation bar
- Several bug fixes and small performance improvements


0.1
----

First stable release
~~~~~~~~~~~~~~~~~~~~

- Upload up to one file per track: contact map, secondary structure, membrane topology, disorder, conservation and custom files
- Support for creation of user accounts, session storage and session sharing
- User contact forms submitted via Slack channel
- Unite testing of modules
- Conducted usability testing with real users
