
loop do
    open('test.out', 'a') do |f|
      f.puts "hello ruby!"
    end

    sleep(rand * 10)
end