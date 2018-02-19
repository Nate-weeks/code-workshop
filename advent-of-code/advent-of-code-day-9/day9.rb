require'pry'



def ignore_characters(input)
  input.each_index do |i|
    if input[i] == "!"
      input.delete_at(i+1)
    end
  end
  input
end

def create_garbage(input)
  i = 0
  while i < input.length
    i += 1
    if input[i] == "<"
      while input[i] != ">"
        i+=1
        break if input[i] == ">"
        input[i] = "a"
      end
    end
  end
  input
end

def count_group(input)
  depth = 0
  count = 0
  input.each do |char|
    if char == '{'
      depth += 1
    end
    if char == '}'
      count += depth
      depth -= 1
    end
  end
  count
end

def test1
  puts "day 9 example: "
  input = File.read("input.txt").split("")
  test_input = "{{<a!>},{<a!>},{<a!>},{<ab>}}".split("")
  result1 = ignore_characters(input)
  result2 = create_garbage(result1)
  result3 = count_group(result2)

  # puts "result1: #{result1} ---- result2: #{result2} ----- result3: #{result3}"
  puts result3
end

test1
