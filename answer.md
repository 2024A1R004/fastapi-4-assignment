1. Why the movie ID should come from the URL instead of the request body?

The URL identifies which record to act on (e.g. PUT /movies/5), so the ID belongs there. Taking it from the URL avoids ambiguity and ID tampering, since the body
should carry only the data to update, not the record's identity.

3. Why PUT should not increase the number of records?
   
PUT updates an existing record, it does not create new ones — that is POST's job. PUT is idempotent, so calling it repeatedly must leave the record count unchanged.
