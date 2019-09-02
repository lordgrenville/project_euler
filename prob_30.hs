toDigits    :: Int -> [Int]
toDigits 0 = []
toDigits x = toDigits (x `div` 10) ++ [x `mod` 10]

isSumofFifth n = n == sum (map (^5) (toDigits n))

main = putStrLn (show ans) 
ans = sum (filter isSumofFifth [9..9999999])
