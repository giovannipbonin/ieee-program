# Announcements

## Citrix Presents: Intro to Angular 2
1. Cool front-end framework.
2. Learn from someone who uses it on the daily

## ACM and IEEE Elections
1. Let me know if you're looking to run for a position
2. Get involved in UHack!
3. Meet future employers
4. Learn through teaching and running programs

# What is Functional Programming?
##  Functions!
1. Pure Functions -> No Side Effects
Not Pure:
```
def append_sum_to_end_of_list_and_return_sum(values):
    total = sum(values)
    values.append(total)
    return total
```
2. Higher Order Functions!
```
numbers = range(100)
def square_me(x):
    return x*x
squared_numbers = map(square_me, numbers)
```
    - `map` is a function that takes a function as an input
    - `map` is a higher order function
3. Recursion Mania!!!
    - Get really excited about recursion!!
    - Lists are all recursive. Think Linked Lists


## Lazy Evaluation
- The following breaks in Python but the equivalent would work in Haskell!
```
print length([2+1, 3*2, 1/0, 5-4])
```

## Immutability
- There are no variables, only values
- You can't change the value of a list. 
- You can create a new list with an old value replaced by a new one
```
# NOPE
x = 5
x = x + 5
```

## Strongly Typed
- You need to declare the types of your variables up front
- The compiler will make sure there are no type conflicts before runtime
- You can't recast variables from one function to another
- In Haskell, the joke is you don't even run your code. You just need to see if it compiles!
- There is plenty of mathematics to make Haskell's type system super powerful

# Haskell!!
## Content Shamelessly Borrowed from `Reading Simple Haskell`
- Original content available [here](https://soupi.github.io/rfc/reading_simple_haskell/).

---

## Definitions - Simple Values

- Left-hand side is the name of the value
- `=` is used to declare the expression that is bound to the name on the left side (value definition)

```hs
five = 5
```

---

## Definitions - Functions

- Add argument names after a name
- Call functions without parentheses

```hs
increment n = n + 1

six = increment five

seven = increment (increment five)

incAndAdd x y = increment x + increment y
```

---

## Definitions - Operators

- You can also define operators

```hs
x +- y = (x + x) - (y + y)
six  = (+-) 5 2
six' = 5 +- 2
```

---

## Function Calls - Partial Application

- We can supply only some of the arguments to a function

```hs
-- takes 3 arguments, so in this case N = 3
sum3 x y z = x + y + z

-- only supplies 2 arguments (K = 2), 0 and 1.
-- so newIncrement is a function that takes (N - K = 1) arguments
newIncrement = sum3 0 1

-- three is the value 3
three = newIncrement 2
```

---

## let/where

- We can name part of the computation using `let` or `where`
- `let [<definition>] in <expression>` is an expression and can be used anywhere
- `where` is special syntax

```hs
sumOf3 x y z =
  let temp = x + y
  in temp + z

-- or:
sumOf3 x y z = temp + z
  where temp = x + y
```

---

## Defining Types

- Concrete types starts with an uppercase letter
- Use `type` to give a new alias to an existing type. They can be used interchangingly.

```hs
type Nickname = String
```

---

## Type Signatures

We can give values a type signature using `::`

```hs
myNickname :: Nickname
myNickname = "suppi"
```

---

## Defining Types - Sum Types

- We can define our own types using the keyword `data`
- Sum types are alternative possible values of a given type
- Similar to enums in other languages
- We use `|` to say "alternatively"
- Each option must start with an uppercase letter
- We can also use `data` to define compound data of existing types
- Similar to structs in other languages

```hs
data KnownColor -- the new type's name
  = Red         -- One possible value
  | Blue
  | Green

redColor :: KnownColor
redColor = Red


data RGB
  = MkRGB Int Int Int
{-
      ^    ^   ^   ^
      |    |   |   |
      |    |   |   +- This is the blue component
      |    |   |
      |    |   +----- This is the green component
      |    |
      |    +--------- This is the red component
      |
      +------------- This is called the value constructor, or "tag"
-}

magenta :: RGB
magenta = MkRGB 255 0 255

-- Or we can combine them!
data Color
  = Red
  | Blue
  | Green
  | RGB Int Int Int

blue :: Color
blue = Blue

magenta :: Color
magenta = RGB 255 0 255
```

---

## The Type of Functions

- We use `->` to denote the type of a function from one type to another type

```hs
increment :: Int -> Int
increment n = n + 1

sum3 :: Int -> Int -> Int -> Int
sum3 x y z = x + y + z

supplyGreenAndBlue :: Int -> Int -> Color
supplyGreenAndBlue = RGB 100
```

---

## The Type of Functions

- `->` is right associative, The function definitions from the previous slide will be parsed like this:

```hs
increment :: Int -> Int
increment n = n + 1

sum3 :: (Int -> (Int -> (Int -> Int)))
sum3 x y z = x + y + z

supplyGreenAndBlue :: (Int -> (Int -> Color))
supplyGreenAndBlue = RGB 100
```

- This is why partial function application works.

---

## Parametric Polymorphism in Type Signatures

```hs
-- I only take concrete `Int` values
identityInt :: Int -> Int
identityInt x = x

five :: Int
five = identityInt 5

-- `a` represents any one type
identity :: a -> a
identity x = x

seven :: Int
seven = identity 7

true :: Bool
true = identity True

const :: a -> b -> a
const x y = x
```

---


## One More Thing About Functions

- In Haskell functions are first class values
- They can be put in variables, passed and returned from functions, etc
- This is a function that takes two functions and a value, applies the second function to the value and then applies the first function to the result
- AKA function composition

```hs
compose :: (b -> c) -> (a -> b) -> a -> c
compose f g x = f (g x)

f . g = compose f g
```

---

## One More Thing About Functions

- Remember, `->` in type signatures is right associative
- Doesn't it look like we take two functions and return a third from the type signature?

```hs
compose :: ((b -> c) -> ((a -> b) -> (a -> c)))
compose f g x = f (g x)
```

---

## Recursive Types and Data Structures

- A recursive data type is a data definition that refers to itself
- This lets us define even more interesting data structures such as linked lists and trees

```hs
data IntList
  = EndOfIntList
  | ValAndNext Int IntList

-- the list [1,2,3]
list123 :: IntList
list123 = ValAndNext 1 (ValAndNext 2 (ValAndNext 3 EndOfList))
```

---

## Case Expression (Pattern Matching)

- Matches from top to bottom

```hs
myIf :: Bool -> a -> a -> a
myIf test trueBranch falseBranch =
  case test of
    True  -> trueBranch
    False -> falseBranch
```

---

## Case Expression (Pattern Matching)

- Matches from top to bottom

```hs
factorial :: Int -> Int
factorial num =
  case num of
    0 -> 1
    n -> n * factorial (n - 1)
```

---

## Case Expression (Pattern Matching)

- Matches from top to bottom
- The pattern `_` means match anything

```hs
colorName :: Color -> String
colorName color =
  case color of
    Red -> "red"
    Green -> "green"
    Blue -> "blue"
    RGB 255 0 255 -> "magenta"
    RGB _ 255 _ -> "well it has a lot of green in it"
    _ -> "i don't know this color"
```

---

## Example

- [Try it in repl.it](https://repl.it/repls/IntrepidVacantGraywolf) to see the result

# Let's Create Lists!
```hs
data List a
  = Nil
  | a :. (List a)

```
- Let's build up from here!
    1. Length of List
    2. Infinite lists
    3. Head and tail
    4. Product of list of ints
    5. Sum of list of ints
    6. Map
    7. Concat two lists
    8. Reverse
    9. Filter
    10. Fold Left, Fold Right

- Some necessary helper code
```hs
infixr 5 :. 

instance Show t => Show (List t) where
  show = show . foldRight (:) []

-- functions over List that you may consider using
foldRight :: (a -> b -> b) -> b -> List a -> b
foldRight _ b Nil      = b
foldRight f b (h :. t) = f h (foldRight f b t)
```
