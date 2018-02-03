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

def test1
  puts "day 9 example: "

  test_input = "{{<a!>},{<a!>},{<a!>},{<ab>}}".split("")
  result1 = ignore_characters(test_input)
  result2 = create_garbage(test_input)

  puts "result1: #{result1} ---- result2: #{result2}"
end

test1
