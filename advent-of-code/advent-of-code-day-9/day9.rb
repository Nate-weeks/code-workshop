require'pry'

input = File.read("input.txt").split("")

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


test_input = "{{<a!>},{<a!>},{<a!>},{<ab>}}".split("")
# test_output = ignore_characters(test_input)
puts create_garbage(ignore_characters(test_input))
