# Customized Implementation of Brownie

In order to automate the process of loading accounts, the default implementation of Brownie was changed in order to provide more control over the CLI. The CLI module was modified in order to use it as an imported library rather than as a part of brownie. This helped us automate the process of authentication which was otherwise required to be done by a user via a CLI.
