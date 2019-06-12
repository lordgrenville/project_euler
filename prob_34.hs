toDigits    :: Int -> [Int]
toDigits 0 = []
toDigits x = toDigits (x `div` 10) ++ [x `mod` 10]

fac = product . flip take [1..]

isCurious :: Int -> Bool
isCurious n = n == sum(map fac (toDigits n))

sum (take 2 (filter isCurious [3..]))
-- taking more than 2 doesn't terminate so we can surmise 2 is the limit?
