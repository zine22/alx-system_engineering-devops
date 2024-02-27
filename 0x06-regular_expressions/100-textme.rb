#!/usr/bin/env ruby
# Make a script about textme

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join
