-- local name="giorgi"
-- local surname="shishniashvili"
-- print(name, surname)

--[[
Task: Simple Number Guessing Game
Objective: Create a simple number guessing game where the computer picks a random number between 1 and 100, and the player has to 
guess it. The program should give feedback on whether the guess is too high or too low, and count how many guesses it takes to get
the  correct number.]]
local secret_num=50
local attempt=0
while true do
    print("Guess the number: ")
    local guess=io.read()
    if guess>secret_num then 
        print("Too high")
    elseif guess<secret_num then
        print("Too low")
    elseif guess==secret_num then
        print("You have guessed the right answer")
    end
end