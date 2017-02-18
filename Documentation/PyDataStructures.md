Python Data Structures  
===  
## Dictionaries and sets 
- key value pair and key, unique
- O(1) lookup and insertion
- takes a lot of space, and needs a fast evaluating hash function
- when hash table has to be resized, indexes are computed again as mask is changed.
-  the smallest size of a dictionary or set is 8. On resize, the number of buckets increases by 4x until we reach 50,000 elements, after which the size is increased by 2x. This gives the following possible sizes,