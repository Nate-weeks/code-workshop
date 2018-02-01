input = [0,	5,	10,	0,	11,	14,	13,	4,	11,	8,	8,	7,	1,	4,	12,	11]


require'pry'
input_array = [] << input.to_s
while input_array.uniq == input_array
  number_to_redistribute = input.max
  index_to_redistribute = input.index(number_to_redistribute)
  max_index = input.length - 1
  input[index_to_redistribute] = 0
  # binding.pry
  while number_to_redistribute > 0
    index_to_redistribute += 1
    if index_to_redistribute > max_index
      index_to_redistribute = 0
    end  
    input[index_to_redistribute] += 1
    number_to_redistribute -= 1
  end
  input_array << input.to_s
  # binding.pry
end
puts input_array.length - 1
binding.pry
