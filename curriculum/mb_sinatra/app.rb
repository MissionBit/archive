# Note: the name of this file (app.rb) is irrelevant.

require 'sinatra'
require 'sinatra/reloader'
require 'csv'

# Don't worry about this method for now
def read_users_from_file(filename)
  CSV.read(filename, :headers => true, :header_converters => :symbol).map { |row| row.to_hash }
end

get '/' do
  "Hello, world!"
end

get '/users' do
  output = "<ol>\n"

  users = read_users_from_file('users.csv')
  users.each do |user|
    output += "<li>\n"
    output += "<a href='/users/#{user[:id]}'>#{user[:first_name]} #{user[:last_name]}</a>\n"
    output += "</li>\n"
  end
  output += "</pre>"

  output
end

get '/users/:id' do
  users = read_users_from_file('users.csv')

  user = users.find { |user| user[:id] == params[:id] }

  if user == nil
    "User #{params[:id]} does not exist"
  else
    "Here's some info for #{user[:first_name]} #{user[:last_name]}"
  end
end
