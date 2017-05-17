##基础部分  

###整数的进制  

十进制：```let d = 17```<br>  
二进制：```let b = 0b00100```<br>  
八进制：```let o = 0o21```<br>  
十六进制: ```let h = 0x1a43```  

###typealias  

```typealias UID = UInt16```  

###布尔  

```let x = true```  

###if  

以下代码不会编译通过<br>  

```  
let x = 1
if x {
}
```  
正确写法  

```  
let x = 1
if x == 1 {
}
```

判断是否有值

```
if let a = b {

}

if let c = d, e = f {
//必须,d和f都有值,该语句才能为真
//否则需要嵌套处理
}
```
### ?和!
```
let possibleString: String? = "An optional string."
let forcedString: String = possibleString! // 需要感叹号来获取值
let assumedString: String! = "An implicitly unwrapped optional string."
let implicitString: String = assumedString  // 不需要感叹号

只有被?类型的变量值才能为nil
?类型的变量需要解包才能进行调用
!类型的变量不需要解包
用!进行解包如果变量没有值则会崩溃，用?则不会
例如：a!.func1() b?.func2()
!可以放在变量后面进行解包赋值，?必须放在调用前面
```

###元组

```
let httpError = (404,"Not Found")
```
关于解包,与python不同,不支持下标访问

```
let (status,msg) = httpError
let httpError2 = (statusCode:200,description:"OK")
let statusCode = httpError2.statusCode
let description = httpError2.description
```

###异常处理

函数抛出异常

```
func canThrowAnError() throws {
}
```

块内抛出异常

```
do {
	try canThrowAnError()
} catch {
	
}
```

多种异常

```
func makeASandwich() throws {

}

do {
} catch SandwichError.outOfCleanDishes {

} catch SandwichError.missingIngredients(let ingredients) {
   
}
```

###断言
```
assert(age >= 0)
assert(age >= 0,"A person's age cannot be less than zero")

注意：
当代码使用优化编译的时候，断言将会被禁用，
例如在 Xcode 中，使用默认的 target Release 
配置选项来 build 时，断言会被禁用。
```

##运算符
### >= 和 <=
swift可以使用>=或者<=进行判断

```
1 >= 1   // true, 因为 1 大于等于 1
2 <= 1   // false, 因为 2 并不小于等于 1
```

###元组的比较
元组大小会按照从左到右、逐值比较的方式，直到发现有两个值不等时停止。如果所有的值都相等，那么这一对元组我们就称它们是相等的。例如：

```
(1, "zebra") < (2, "apple")   // true，因为 1 小于 2
(3, "apple") < (3, "bird")    // true，因为 3 等于 3，但是 apple 小于 bird
(4, "dog") == (4, "dog")      // true，因为 4 等于 4，dog 等于 dog
```

###空合运算符
`a ?? b`<br>
可以表示<br>
`a != nil ? a! : b`<br>
如果a不等于空取a(强制解包)的值,否则取b

```
let defaultColorName = "red"
var userDefinedColorName: String?   //默认值为 nil

var colorNameToUse = userDefinedColorName ?? defaultColorName
// userDefinedColorName 的值为空，所以 colorNameToUse 的值为 "red"
```

###区间运算符
`a...b`表示定义一个闭区间(包括a和b的值):

```
for i in 1...5 :
	print(i)  //打印1，2，3，4，5
```

`a..<b`表示定义一个半开区间(包括a的值，不包括b的值)

```
for i in 1..<5 :
	print(i)  //打印1，2，3，4
```

##字符与字符串
###字符串常量
字符串常量，必须有加@

```
let someStr = "abcdef"
```

###字符串支持+和+=操作
```
var myStr = "a"
myStr += "b"
let a_str = "a"
let b_str = "b"
let c_str = a_str+b_str
注意：
您不能将一个字符串或者字符添加到一个
已经存在的字符变量上，因为字符变量只能包含一个字符。
```

###字符串是值类型
任何情况下，都会对已有字符串值创建新副本，并对该新副本进行传递或赋值操作。

###使用字符
```
let c_a:Character = "a"

for character in "Dog!🐶".characters {
    print(character)
}
// D
// o
// g
// !
// 🐶
```

###字符串插值
```
let multiplier = 3
let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"

注意：
插值字符串中写在括号中的表达式不能包含非转义反斜杠 (\)，
并且不能包含回车或换行符。不过，插值字符串可以包含其他字面量。
```

###Unicode标量
```
let dollarSign = "\u{24}"    // $, Unicode 标量 U+0024
let blackHeart = "\u{2665}"  // ♥, Unicode 标量 U+2665
let sparklingHeart = "\u{1F496}"// 💖, Unicode 标量U+1F496
```
###计算字符数量
```
let unusualMenagerie = "Koala 🐨, Snail 🐌, Penguin 🐧, Dromedary 🐪"
print("unusualMenagerie has \(unusualMenagerie.characters.count) characters")
// 打印输出 "unusualMenagerie has 40 characters"

注意：
可扩展的字符群集可以组成一个或者多个 Unicode 标量。
这意味着不同的字符以及相同字符的不同表示方式可能需要不同
数量的内存空间来存储。所以 Swift 中的字符在一个字符串中并
不一定占用相同的内存空间数量。因此在没有获取字符串的可扩展
的字符群的范围时候，就不能计算出字符串的字符数量。如果您正
在处理一个长字符串，需要注意characters属性必须遍历全部
的 Unicode 标量，来确定字符串的字符数量。

另外需要注意的是通过characters属性返回的字符数量并不总是
与包含相同字符的NSString的length属性相同。NSString的
length属性是利用 UTF-16 表示的十六位代码单元数字，而不
是 Unicode 可扩展的字符群集。
```

###字符串比较
字符串/字符可以用等于操作符(==)和不等于操作符(!=)

```
let quotation = "We're a lot alike, you and I."
let sameQuotation = "We're a lot alike, you and I."
if quotation == sameQuotation {
    print("These two strings are considered equal")
}
// 打印输出 "These two strings are considered equal"

注意：
在 Swift 中，字符串和字符并不区分地域。
```

###UTF-8表示
您可以通过遍历String的utf8属性来访问它的UTF-8表示。 其为String.UTF8View类型的属性，UTF8View是无符号8位 (UInt8) 值的集合

```
for codeUnit in dogString.utf8 {
    print("\(codeUnit) ", terminator: "")
}
print("")
// 68 111 103 226 128 188 240 159 144 182
```

###UTF-16表示
同上

###Unicode 标量表示
您可以通过遍历String值的unicodeScalars属性来访问它的 Unicode 标量表示。 其为UnicodeScalarView类型的属性，UnicodeScalarView是UnicodeScalar类型的值的集合。

```
for scalar in dogString.unicodeScalars {
    print("\(scalar.value) ", terminator: "")
}
print("")
// 68 111 103 8252 128054
```

##集合框架
###三种集合类型
Swift 语言提供`Arrays`、`Sets`和`Dictionaries`三种基本的集合类型用来存储集合数据。

###集合可变性
通过let和var区分是否可变

###创建一个空数组
`var someInts = [Int]()`

###创建一个带有默认值的数组
`var threeDoubles = Array(repeating: 0.0, count: 3)`

###数组支持+和+=运算符
数组之间可以用+和+=方法

```
var arr_x = [1,2,3]
arr_x += [4,5]
```

###判断数组为空
isEmpty可以判断数组是否为空，其等价于count==0

###可以用区间批量改变数组的值
```
var arr_x = [1,2,3]
arr_x[1...2] = [10,10] //arr_x此时为[1,10,10]
```

###用enumerated遍历数组
```
for (index, value) in shoppingList. enumerated() {
    print("Item \(String(index + 1)): \(value)")
}
```

###创建和构造一个空的集合
`var letters = Set<Character>()`

###可以用数组字面量创建一个集合
```
var favoriteGenres: Set<String> = ["Rock", "Classical", "Hip hop"]
```

###集合操作
- 使用intersection(_:)方法根据两个集合中都包含的值创建的一个新的集合。
- 使用symmetricDifference(_:)方法根据在一个集合中但不在两个集合中的值创建一个新的集合。
- 使用union(_:)方法根据两个集合的值创建一个新的集合。
- 使用subtracting(_:)方法根据不在该集合中的值创建一个新的集合。
- 使用“是否相等”运算符(==)来判断两个集合是否包含全部相同的值。
- 使用isSubset(of:)方法来判断一个集合中的值是否也被包含在另外一个集合中。
- 使用isSuperset(of:)方法来判断一个集合中包含另一个集合中所有的值。
- 使用isStrictSubset(of:)或者isStrictSuperset(of:)方法来判断一个集合是否是另外一个集合的子集合或者父集合并且两个集合并不相等。
- 使用isDisjoint(with:)方法来判断两个集合是否不含有相同的值(是否没有交集)。

###创建一个空字典
`var namesOfIntegers = [Int: String]()`

###字典字面量
```
var airports: [String: String] = 
["YYZ": "Toronto Pearson", "DUB": "Dublin"]
```
###字典遍历
```
for (airportCode, airportName) in airports {
    print("\(airportCode): \(airportName)")
}
```

##控制流
###使用匿名变量遍历
当你不需要知道下表的时候，你可以使用如下代码

```
var answer = 1
let base = 3
for _ in 1...100 {
    answer *= base
}
```

设置步长的遍历

```
for i in stride(from: 0, to: 10, by: 2) {
    print(i)
    //会打印0，2，4，6，8，不会取到10，如果想取到10，那家写11
}

for i in stride(from: 0, through: 10, by: 2) {
    print(i)
    //会打印0，2，4，6，8，10
}
```
###Repeat-While循环
Swift语言的repeat-while循环和其他语言中的do-while循环是类似的。

###支持区间的Switch
```
let approximateCount = 62
var naturalCount: String
switch approximateCount {
case 0:
    naturalCount = "no"
case 1..<5:
    naturalCount = "a few"
case 5..<12:
    naturalCount = "several"
case 12..<100:
    naturalCount = "dozens of"
case 100..<1000:
    naturalCount = "hundreds of"
default:
    naturalCount = "many"
}
```
###Switch中的元组
我们可以使用元组在同一个switch语句中测试多个值。元组中的元素可以是值，也可以是区间。另外，使用下划线（_）来匹配所有可能的值。

```
let somePoint = (1, 1)
switch somePoint {
case (0, 0):
    print("(0, 0) is at the origin")
case (_, 0):
    print("(\(somePoint.0), 0) is on the x-axis")
case (0, _):
    print("(0, \(somePoint.1)) is on the y-axis")
case (-2...2, -2...2):
    print("(\(somePoint.0), \(somePoint.1)) is inside the box")
default:
    print("(\(somePoint.0), \(somePoint.1)) is outside of the box")
}
```

###Switch值绑定
```
let anotherPoint = (2, 0)
switch anotherPoint {
case (let x, 0):
    print("on the x-axis with an x value of \(x)")
case (0, let y):
    print("on the y-axis with a y value of \(y)")
case let (x, y):
    print("somewhere else at (\(x), \(y))")
}
// 输出 "on the x-axis with an x value of 2"
```
###Switch中可以加入Where
```
let yetAnotherPoint = (1, -1)
switch yetAnotherPoint {
case let (x, y) where x == y:
    print("(\(x), \(y)) is on the line x == y")
case let (x, y) where x == -y:
    print("(\(x), \(y)) is on the line x == -y")
case let (x, y):
    print("(\(x), \(y)) is just some arbitrary point")
}
```

###Switch组合匹配
```
let someCharacter: Character = "e"
switch someCharacter {
case "a", "e", "i", "o", "u":
    print("\(someCharacter) is a vowel")
case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
     "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
    print("\(someCharacter) is a consonant")
default:
    print("\(someCharacter) is not a vowel or a consonant")
}
```

###Switch,For,Continue
```
let puzzleInput = "great minds think alike"
var puzzleOutput = ""
for character in puzzleInput.characters {
    switch character {
    case "a", "e", "i", "o", "u", " ":
        continue
    default:
        puzzleOutput.append(character)
    }
}
print(puzzleOutput)
```

###Switch贯穿
C语言中，你必须显示的调用break，才能跳过其他的分支，
而Swift刚好与之相反，只要匹配到了一个分支，switch就结束了，你可以通过在分支下面加入fallthrough来实现
C语言的switch

```
let integerToDescribe = 5
var description = "The number \(integerToDescribe) is"
switch integerToDescribe {
case 2, 3, 5, 7, 11, 13, 17, 19:
    description += " a prime number, and also"
    fallthrough
default:
    description += " an integer."
}
print(description)

注意： fallthrough关键字不会检查它下一个将会落入执行的 
case 中的匹配条件。fallthrough简单地使代码继续连接
到下一个 case 中的代码，这和 C 语言标准中的switch语
句特性是一样的。
```

###Continue,Break的标签
当你有多层嵌套循环的时候，你可以用continue/break label来实现
跳过指定的循环层

```
gameLoop: while square != finalSquare {
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    switch square + diceRoll {
    case finalSquare:
        // 骰子数刚好使玩家移动到最终的方格里，游戏结束。
        break gameLoop
    case let newSquare where newSquare > finalSquare:
        // 骰子数将会使玩家的移动超出最后的方格，那么这种移动是不合法的，玩家需要重新掷骰子
        continue gameLoop
    default:
        // 合法移动，做正常的处理
        square += diceRoll
        square += board[square]
    }
}
print("Game over!")
```
###guard
像if语句一样，guard的执行取决于一个表达式的布尔值。我们可以使用guard语句来要求条件必须为真时，以执行guard语句后的代码。不同于if语句，一个guard语句总是有一个else从句，如果条件不为真则执行else从句中的代码。(用于对允许值的过滤，往往不允许的值的条件，会让
代码可读性变差，也有可能写漏)

```
func greet(person: [String: String]) {
    guard let name = person["name"] else {
        return
    }
    print("Hello \(name)")
    guard let location = person["location"] else {
        print("I hope the weather is nice near you.")
        return
    }
    print("I hope the weather is nice in \(location).")
}
greet(["name": "John"])
// 输出 "Hello John!"
// 输出 "I hope the weather is nice near you."
greet(["name": "Jane", "location": "Cupertino"])
// 输出 "Hello Jane!"
// 输出 "I hope the weather is nice in Cupertino."
```

###检测API是否可用
```
if #available(iOS 10, macOS 10.1,*) {
    
}
```

##函数
###函数定义
```
func greet(person: String, alreadyGreeted: Bool)
 -> String {
}

greet(person: "Tim", alreadyGreeted: true)
```

###无返回值函数
```
func greet(person: String) {
    print("Hello, \(person)!")
}
greet(person: "Dave")
```

###多重返回值函数
```
func minMax(array: [Int]) -> (min: Int, max: Int) {
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}

let bounds = minMax(array: [8, -6, 2, 109, 3, 71])
print("min is \(bounds.min) and max is \(bounds.max)")
```

###可选元组返回类型
```
注意 可选元组类型如 (Int, Int)? 与元组包含可选类型如 
(Int?, Int?) 是不同的.可选的元组类型，整个元组是可选
的，而不只是元组中的每个元素值。
```

###指定参数标签
```
func greet(person: String, from hometown: String)
 -> String {
    return "Hello \(person)!  Glad you could visit from \(hometown)."
}
greet(person: "Bill", from: "Cupertino")
```

###忽略参数标签
如果你不希望为某个参数添加一个标签，可以使用一个下划线(_)来代替一个明确的参数标签

```
func someFunction(_ firstParameterName: Int, secondParameterName: Int) {
     // 在函数体内，firstParameterName 和 secondParameterName 代表参数中的第一个和第二个参数值
}
someFunction(1, secondParameterName: 2)
```

###模式参数值
将不带有默认值的参数放在函数参数列表的最前。一般来说，没有默认值的参数更加的重要，将不带默认值的参数放在最前保证在函数调用时，非默认参数的顺序是一致的，同时也使得相同的函数在不同情况下调用时显得更为清晰。

```
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // 如果你在调用时候不传第二个参数，parameterWithDefault 会值为 12 传入到函数体中。
}
```

###可变参数
```
func arithmeticMean(_ numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }
    return total / Double(numbers.count)
}
arithmeticMean(1, 2, 3, 4, 5)

注意：
一个函数最多只能拥有一个可变参数。
```

###输入输出参数
```
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
// 打印 "someInt is now 107, and anotherInt is now 3"
```

###使用函数类型
```
var mathFunction: (Int, Int) -> Int = addTwoInts

func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Result: \(mathFunction(a, b))")
}

func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    return backward ? stepBackward : stepForward
}
```

###嵌套函数
```
func chooseStepFunction(backward: Bool) 
-> (Int) -> Int {
    func stepForward(input: Int) -> Int {
     return input + 1
    }
    func stepBackward(input: Int) -> Int {
     return input - 1 
    }
    return backward ? stepBackward : stepForward
}
```
