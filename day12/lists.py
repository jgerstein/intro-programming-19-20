things = [
    'abacus', 'bean kamen', 'cockadoodledoo',
    'didgeridoo', 'elephantitis', 'fibula',
    'google', 'strange children', 'hypothermia',
    'indigenous species', 'jamaica', 'kangaroo',
    'very strange children', 'the strangest children',
    'ligament', 'melody', 'nice children. nice but very strange',
    'optimus', 'prime', 'questionable sanity', 'rodeo',
    'succulents', 'typhoid', 'understandably confused children',
    'ventricle', 'vesuvius', 'wagner matinee',
    'xavier', 'xylophone', 'yoink', 'why',
    'zebra', 'zubat', 'zeus', 'zucchini', 'zucculent',
    'the absolute strangest class',
    'actually the second strangest', 'ethan'
]
nums = [100, -35, 42, 5000, 78, 987, 254, 136]
smallest = 1000000

for num in nums:
    if num < smallest:
        smallest = num

print(smallest)