import array
import random
import time


def timeit(f):
    """ decorator code for timing function calls """

    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print("func:%r args: [%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))

        return result

    return timed


@timeit
def dimensions():
    """ function code for array input requests """

    dimension_input = []

    # Row Count input request. If not an integer value, try again.
    while True:
        try:
            row_count = int(input("What is the Row Count? "))
            break
        except ValueError:
            print("Please input an integer value for Row Count. ")
            continue

        # Column Count input request. If not an integer value, try again.
    while True:
        try:
            column_count = int(input("What is the Column Count? "))
            break
        except ValueError:
            print("Please input an integer value for the Column Count. ")
            continue

        # Intended Range input request. If not an integer value, try again.
        # If count is larger than row or column count, try again.
    while True:
        try:
            range_count = int(input("What is the Numeric Range? "))
            if range_count > column_count and range_count > row_count:
                print(
                    "The Range must be less than the Row Max:",
                    row_count,
                    " and Column Max:",
                    column_count,
                    ". Try again. ",
                )
                continue
            elif range_count > column_count:
                print("The Range must be less than the Column Count. Try again. ")
                continue
            elif range_count > row_count:
                print("The Range must be less than the Row Count. Try again. ")
                continue
            else:
                break
        except ValueError:
            print("Please input an integer value for Range. ")
            continue

    dimension_input.append(row_count)
    dimension_input.append(column_count)
    dimension_input.append(range_count)

    return dimension_input


@timeit
def manhattan_distance(input_count):
    """ function code for array calculations  """

    row_count = input_count[0]  # row_count reference (H / Y axis)
    column_count = input_count[1]  # column_count reference (W / X axix)
    range_count = input_count[2]  # count_range reference (N / threshold)

    # Define the arrays
    int_array = [[0 for x in range(column_count)] for y in range(row_count)] # Integer Array initialized to 0, static size.
    xyArray=([]) # Coordinate Array
    man_array=([]) # Manhattan Array
    culm_array=([]) # Culmunative Array
    unique_items_array=([]) # Unique Array
    overlap_items_array=([]) # Overlap Array

    # Populate the integer array
    current_row_index=0
    current_column_index=0
    for row in int_array:
        for column in row:
            temp_value = random.randint(-99,1)
            int_array[current_row_index][current_column_index] = temp_value
            # add positive value to coordinate array
            if temp_value > 0: 
                xyArray.append([current_row_index,current_column_index])
            # if column index reaches column limit, set to 0, else increment
            if current_column_index == column_count - 1:
                current_column_index = 0
            else:
                current_column_index = current_column_index + 1
        # if row index reaches row limit, set to 0, else increment
        if current_row_index == row_count - 1:
            current_row_index = 0
        else:	
            current_row_index = current_row_index + 1

    # Show the Array by each row
    print("========================"*3)
    for row in int_array:
        print(row)

    # show the positive coordiates and manhattan coordinates to each positive
    print("========================"*3)
    print("Positives found:",len(xyArray))
    print("Coordinates (Row,Column) Starts @ 0:",xyArray)
    print("========================"*3)
    sum = 0
    current_row_index=0
    current_column_index=0
    # break the positive coordinate array into values
    for xy_coord in xyArray:
        x=xy_coord[0]
        y=xy_coord[1]
        if current_column_index == 0: 
            print("")
            print("")
            print("========================"*3)
            print("The cells within a",range_count,"range of (",x,",",y,")")
            print("------------------------"*3)
    #	check the positive coordinates against each coordinate in the full integer array to see if it is within the manhattan distance range
        for row in int_array:
            for column in row:		
                if (abs(x - current_row_index) + abs(y - current_column_index)) <= range_count:
                    sum=sum+1		
                    # save to the manhattan array
                    man_array.append([current_row_index,current_column_index])
                    # save to a culmulative array for all manhattan coordinates for unique and overlap checks later
                    culm_array.append([current_row_index,current_column_index])
                # reset column count to 0 when reaches entered column count, if not increment count
                if current_column_index == column_count - 1:
                    current_column_index = 0
                else:
                    current_column_index = current_column_index + 1
            # reset row count to 0 when reaches entered row count, if not increment count
            if current_row_index == row_count - 1:
                current_row_index = 0
            else:	
                current_row_index = current_row_index + 1
            # if array has values, print then clear. if not then clear
            if len(man_array) > 0:
                print(man_array)
                man_array=([])
            else:
                man_array=([])
        # print header for neighbors
        print("------------------------"*3)
        print("Neighbors total found for: (",x,",",y,") is",sum)
        print("========================"*3)
        sum=0
    culm_array.sort()
    # check culmulative array for overlap values, then write to overlap if present or write to unique if not present
    for item in culm_array:
        if item in unique_items_array: 
            overlap_items_array.append(item)
        else:
            unique_items_array.append(item)
    # remove items from unique that were later detemined to overlap
    for item in overlap_items_array:
        if item in unique_items_array:
            unique_items_array.remove(item)
            
    print("")
    print("")
    unique_items_array.sort()
    overlap_items_array.sort()
    #print headers for unique value, then values
    print("========================"*3)
    print("Total Unique Neighbors in Array:",len(unique_items_array),"Percent:",round(len(unique_items_array)/(row_count*column_count)*100,2))
    print("========================"*3)
    print(unique_items_array)
    print("========================"*3)
    print("")
    print("")
    #print header for overlaping values, then values
    print("========================"*3)
    print("Total overlapping Neighbors in Array:",len(overlap_items_array),"Percent:",round(len(overlap_items_array)/(row_count*column_count)*100,2))
    print("========================"*3)
    print(overlap_items_array)
    print("========================"*3)


@timeit
def main():
    """ function code for passing arguments between functions """

    dimension_input = dimensions()
    manhattan_distance(dimension_input)


if __name__ == "__main__":
    main()
