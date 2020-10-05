Artwork Database Program
Ben Haseltine
4 October 2020

The Artwork Database Program utilizes a Peewee ORM to allow users to add, query, and delete artists and artworks from persistence storage in a Sqlite database.

This program uses a semi-MVVM structure with a validation module between the view and the viewmodel.
The user chooses an option from the menu, which sends it to a function to send to the validation module.
The validation module contains methods that make sure user-input conforms to the data the viewmodel is expecting, then sends back to main to send to the viewmodel.
Finally, the viewmodel sends the data to the database to be inserted, queried, or deleted.