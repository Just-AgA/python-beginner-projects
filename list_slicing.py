#Using the slice() function to slice and reverse list chunks

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

start = 0
chunk_size = int(len(sample_list) / 3)
end = chunk_size


# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size