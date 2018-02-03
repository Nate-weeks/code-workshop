input = [0,	5,	10,	0,	11,	14,	13,	4,	11,	8,	8,	7,	1,	4,	12,	11]


require'pry'
# input_array = [] << input.to_s
# while input_array.uniq == input_array
#   number_to_redistribute = input.max
#   index_to_redistribute = input.index(number_to_redistribute)
#   max_index = input.length - 1
#   input[index_to_redistribute] = 0
#   # binding.pry
#   while number_to_redistribute > 0
#     index_to_redistribute += 1
#     if index_to_redistribute > max_index
#       index_to_redistribute = 0
#     end
#     input[index_to_redistribute] += 1
#     number_to_redistribute -= 1
#   end
#   input_array << input.to_s
#   # binding.pry
# end
# puts input_array.length - 1
# binding.pry

def redistribute(input)
  number_to_redistribute = input.max
  index_to_redistribute = input.index(number_to_redistribute)
  input[index_to_redistribute] = 0

  while number_to_redistribute > 0
    index_to_redistribute = (index_to_redistribute + 1) % input.length
    input[index_to_redistribute] += 1
    number_to_redistribute -= 1
  end
  input
end

def repeat(input, part)
  results = [] << input.to_s
  while results.uniq == results
    input = redistribute(input)
    results << input.to_s
  end
  if part == 1
  return results.length - 1
  elsif part == 2
  return results[results.length-1]
  end
end


array = eval(repeat(input, 2))
binding.pry
puts array
puts repeat(array, 1)
