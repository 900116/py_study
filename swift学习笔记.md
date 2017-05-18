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
```

```
注意：
当代码使用优化编译的时候，断言将会被禁用，例如在 Xcode 中，使用默认的 target Release 配置选项来 build 时，断言会被禁用。
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
```

```
注意：
您不能将一个字符串或者字符添加到一个已经存在的字符变量上，因为字符变量只能包含一个字符。
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
```

```
注意：
插值字符串中写在括号中的表达式不能包含非转义反斜杠 (\)，并且不能包含回车或换行符。不过，插值字符串可以包含其他字面量。
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
```

```
注意：
可扩展的字符群集可以组成一个或者多个 Unicode 标量。这意味着不同的字符以及相同字符的不同表示方式可能需要不同数量的内存空间来存储。所以 Swift 中的字符在一个字符串中并不一定占用相同的内存空间数量。因此在没有获取字符串的可扩展的字符群的范围时候，就不能计算出字符串的字符数量。如果您正在处理一个长字符串，需要注意characters属性必须遍历全部的 Unicode 标量，来确定字符串的字符数量。

另外需要注意的是通过characters属性返回的字符数量并不总是与包含相同字符的NSString的length属性相同。NSString的length属性是利用 UTF-16 表示的十六位代码单元数字，而不是 Unicode 可扩展的字符群集。
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
case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m","n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
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
C语言中，你必须显示的调用break，才能跳过其他的分支，而Swift刚好与之相反，只要匹配到了一个分支，switch就结束了，你可以通过在分支下面加入fallthrough来实现C语言的switch

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
```

```
注意： fallthrough关键字不会检查它下一个将会落入执行的 case 中的匹配条件。fallthrough简单地使代码继续连接到下一个 case 中的代码，这和 C 语言标准中的switch语句特性是一样的。
```

###Continue,Break的标签
当你有多层嵌套循环的时候，你可以用continue/break label来实现跳过指定的循环层

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
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int {
     return input + 1
    }
    func stepBackward(input: Int) -> Int {
     return input - 1 
    }
    return backward ? stepBackward : stepForward
}
```

##闭包
###闭包表达式语法
```
reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```
###根据上下文推断类型
因为排序闭包函数是作为 sorted(by:) 方法的参数传入的，Swift 可以推断其参数和返回值的类型。sorted(by:) 方法被一个字符串数组调用，因此其参数必须是 (String, String) -> Bool 类型的函数。这意味着 (String, String) 和 Bool 类型并不需要作为闭包表达式定义的一部分。因为所有的类型都可以被正确推断，返回箭头（->）和围绕在参数周围的括号也可以被省略：

```
reversedNames = names.sorted(by: 
{ s1, s2 in return s1 > s2 } )
```

###单表达式闭包隐式返回
单行表达式闭包可以通过省略 return 关键字来隐式返回单行表达式的结果。

```
reversedNames = names.sorted(by: { s1, s2 in s1 > s2 } )
```

###参数名称缩写
Swift 自动为内联闭包提供了参数名称缩写功能，你可以直接通过 $0，$1，$2 来顺序调用闭包的参数，以此类推。

```
reversedNames = names.sorted(by: { $0 > $1 } )
```

###运算符方法
实际上还有一种更简短的方式来编写上面例子中的闭包表达式。Swift 的 String 类型定义了关于大于号（>）的字符串实现，其作为一个函数接受两个 String 类型的参数并返回 Bool 类型的值。而这正好与 sorted(by:) 方法的参数需要的函数类型相符合。

```
reversedNames = names.sorted(by: >)
```

###尾随闭包
果你需要将一个很长的闭包表达式作为最后一个参数传递给函数，可以使用尾随闭包来增强函数的可读性

```
func someFunctionThatTakesAClosure(closure: () -> Void) {
    // 函数体部分
}

// 以下是不使用尾随闭包进行函数调用
someFunctionThatTakesAClosure(closure: {
    // 闭包主体部分
})

// 以下是使用尾随闭包进行函数调用
someFunctionThatTakesAClosure() {
    // 闭包主体部分
}

reversedNames = names.sorted() { $0 > $1 }
reversedNames = names.sorted { $0 > $1 }
```

##闭包逃逸
当一个闭包作为参数传到一个函数中，但是这个闭包在函数返回之后才被执行，我们称该闭包从函数中逃逸。当你定义接受闭包作为参数的函数时，你可以在参数名之前标注 @escaping，用来指明这个闭包是允许“逃逸”出这个函数的。

```
var completionHandlers: [() -> Void] = []
func someFunctionWithEscapingClosure(completionHandler: @escaping () -> Void) {
    completionHandlers.append(completionHandler)
}
```

someFunctionWithEscapingClosure(_:) 函数接受一个闭包作为参数，该闭包被添加到一个函数外定义的数组中。如果你不将这个参数标记为 @escaping，就会得到一个编译错误。

将一个闭包标记为 @escaping 意味着你必须在闭包中显式地引用 self。

```
func someFunctionWithNonescapingClosure(closure:() -> Void) {
    closure()
}

class SomeClass {
    var x = 10
    func doSomething() {
        someFunctionWithEscapingClosure { 
        self.x = 100 }
        someFunctionWithNonescapingClosure { 
        x = 200 }
    }
}
```

###自动闭包
自动闭包是一种自动创建的闭包，用于包装传递给函数作为参数的表达式。这种闭包不接受任何参数，当它被调用的时候，会返回被包装在其中的表达式的值。这种便利语法让你能够省略闭包的花括号，用一个普通的表达式来代替显式的闭包。

```
// customersInLine is ["Alex", "Ewa", "Barry", "Daniella"]
func serve(customer customerProvider: () -> String) {
    print("Now serving \(customerProvider())!")
}
serve(customer: { customersInLine.remove(at: 0) } )
// 打印出 "Now serving Alex!"
```

下面这个版本的 serve(customer:) 完成了相同的操作，不过它并没有接受一个显式的闭包，而是通过将参数标记为 @autoclosure 来接收一个自动闭包。现在你可以将该函数当作接受 String 类型参数（而非闭包）的函数来调用。customerProvider 参数将自动转化为一个闭包，因为该参数被标记了 @autoclosure 特性。

```
// customersInLine is ["Ewa", "Barry", "Daniella"]
func serve(customer customerProvider: 
@autoclosure () -> String) {
    print("Now serving \(customerProvider())!")
}
serve(customer: customersInLine.remove(at: 0))
// 打印 "Now serving Ewa!"
```

```
注意 过度使用 autoclosures 会让你的代码变得难以理解。上下文和函数名应该能够清晰地表明求值是被延迟执行的。
```

如果你想让一个自动闭包可以“逃逸”，则应该同时使用@autoclosure 和 @escaping 属性。

```
// customersInLine i= ["Barry", "Daniella"]
var customerProviders: [() -> String] = []
func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
    customerProviders.append(customerProvider)
}
collectCustomerProviders(customersInLine.remove(at: 0))
collectCustomerProviders(customersInLine.remove(at: 0))

print("Collected \(customerProviders.count) closures.")
// 打印 "Collected 2 closures."
for customerProvider in customerProviders {
    print("Now serving \(customerProvider())!")
}
// 打印 "Now serving Barry!"
// 打印 "Now serving Daniella!"
```

##枚举
###枚举语法
```
enum CompassPoint {
    case north
    case south
    case east
    case west
}

var directionToHead = CompassPoint.west
directionToHead = .east
```

```
注意
与 C 和 Objective-C 不同，Swift 的枚举成员在被创建时不会被赋予一个默认的整型值。在上面的CompassPoint例子中，north，south，east和west不会被隐式地赋值为0，1，2和3。相反，这些枚举成员本身就是完备的值，这些值的类型是已经明确定义好的CompassPoint类型。
```
当directionToHead的类型已知时，再次为其赋值可以省略枚举类型名。在使用具有显式类型的枚举值时，这种写法让代码具有更好的可读性。
###多个值可以出现在同一行
```
enum Planet {
    case mercury, venus, earth, mars, 
    jupiter, saturn, uranus, neptune
}
```

###使用 Switch 语句匹配枚举值
```
directionToHead = .south
switch directionToHead {
    case .north:
        print("Lots of planets have a north")
    case .south:
        print("Watch out for penguins")
    case .east:
        print("Where the sun rises")
    case .west:
        print("Where the skies are blue")
}
// 打印 "Watch out for penguins”
```
正如在控制流中介绍的那样，在判断一个枚举类型的值时，switch语句必须穷举所有情况。如果忽略了.west这种情况，上面那段代码将无法通过编译，因为它没有考虑到CompassPoint的全部成员。强制穷举确保了枚举成员不会被意外遗漏。

当不需要匹配每个枚举成员的时候，你可以提供一个default分支来涵盖所有未明确处理的枚举成员：

```
let somePlanet = Planet.earth
switch somePlanet {
case .earth:
    print("Mostly harmless")
default:
    print("Not a safe place for humans")
}
// 打印 "Mostly harmless”
```

###关联值
```
enum Barcode {
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}

var productBarcode = Barcode.upc(8, 85909, 51226, 3)
productBarcode = .qrCode("ABCDEFGHIJKLMNOP")

switch productBarcode {
case .upc(let numberSystem, let manufacturer, 
let product, let check):
    print("UPC: \(numberSystem), \(manufacturer),
     \(product), \(check).")
case .qrCode(let productCode):
    print("QR code: \(productCode).")
}
// 打印 "QR code: ABCDEFGHIJKLMNOP."
```

如果一个枚举成员的所有关联值都被提取为常量，或者都被提取为变量，为了简洁，你可以只在成员名称前标注一个let或者var：

```
case let .upc(numberSystem, manufacturer, 
product, check):
    print("UPC: \(numberSystem),
     \(manufacturer), \(product), \(check).")
case let .qrCode(productCode):
    print("QR code: \(productCode).")
}
// 输出 "QR code: ABCDEFGHIJKLMNOP."
```

###原始值
```
enum ASCIIControlCharacter: Character {
    case tab = "\t"
    case lineFeed = "\n"
    case carriageReturn = "\r"
}

注意
原始值和关联值是不同的。原始值是在定义枚举时被预先填充的值，像上述三个 ASCII 码。对于一个特定的枚举成员，它的原始值始终不变。关联值是创建一个基于枚举成员的常量或变量时才设置的值，枚举成员的关联值可以变化。
```

###原始值的隐式赋值
```
enum Planet: Int {
    case mercury = 1, venus, earth, mars,
     jupiter, saturn, uranus, neptune
}

let earthsOrder = Planet.earth.rawValue
// earthsOrder 值为 3

let sunsetDirection = CompassPoint.west.rawValue
// sunsetDirection 值为 "west"
```
在上面的例子中，Plant.mercury的显式原始值为1，Planet.venus的隐式原始值为2，依次类推。

```
enum CompassPoint: String {
    case north, south, east, west
}
```

###使用原始值初始化枚举实例
```
let possiblePlanet = Planet(rawValue: 7)
// possiblePlanet 类型为 Planet? 值为 Planet.uranus
```

##递归枚举
递归枚举是一种枚举类型，它有一个或多个枚举成员使用该枚举类型的实例作为关联值。使用递归枚举时，编译器会插入一个间接层。你可以在枚举成员前加上indirect来表示该成员可递归。

```
enum ArithmeticExpression {
    case number(Int)
    indirect case addition(ArithmeticExpression, ArithmeticExpression)
    indirect case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```

你也可以在枚举类型开头加上`indirect`关键字来表明它的所有成员都是可递归的：

```
indirect enum ArithmeticExpression {
    case number(Int)
    case addition(ArithmeticExpression, ArithmeticExpression)
    case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```
例如，表达式(5 + 4) * 2，乘号右边是一个数字，左边则是另一个表达式。因为数据是嵌套的，因而用来存储数据的枚举类型也需要支持这种嵌套——这意味着枚举类型需要支持递归。

要操作具有递归性质的数据结构，使用递归函数是一种直截了当的方式。例如，下面是一个对算术表达式求值的函数：

```
func evaluate(_ expression: ArithmeticExpression) -> Int {
    switch expression {
    case let .number(value):
        return value
    case let .addition(left, right):
        return evaluate(left) + evaluate(right)
    case let .multiplication(left, right):
        return evaluate(left) * evaluate(right)
    }
}

print(evaluate(product))
// 打印 "18"
```

##类
###类和结构体对比
共同点:<br>

- 定义属性用于存储值  
- 定义方法用于提供功能  
- 定义下标操作使得可以通过下标语法来访问实例所包含的值  
- 定义构造器用于生成初始化值  
- 通过扩展以增加默认实现的功能  
- 实现协议以提供某种标准功能  

与结构体相比，类还有如下的附加功能：

- 继承允许一个类继承另一个类的特征
- 类型转换允许在运行时检查和解释一个类实例的类型
- 析构器允许一个类实例释放任何其所被分配的资源
- 引用计数允许对一个类的多次引用

```
注意
结构体总是通过被复制的方式在代码中传递，不使用引用计数。
```

###定义语法
```
struct Resolution {
    var width = 0
    var height = 0
}
class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}
```

###属性
与 Objective-C 语言不同的是，Swift 允许直接设置结构体属性的子属性。上面的最后一个例子，就是直接设置了someVideoMode中resolution属性的width这个子属性，以上操作并不需要重新为整个resolution属性设置新值。

###结构体类型的成员逐一构造器
```
let vga = Resolution(width:640, height: 480)
```

###结构体和枚举是值类型,类是引用类型
###恒等运算符
- 等价于（===）
- 不等价于（!==）

```
f tenEighty === alsoTenEighty {
    print("tenEighty and alsoTenEighty refer to the same Resolution instance.")
}
//打印 "tenEighty and alsoTenEighty refer to the same Resolution instance."
```

请注意，“等价于”（用三个等号表示，===）与“等于”（用两个等号表示，==）的不同：

- “等价于”表示两个类类型（class type）的常量或者
   变量引用同一个类实例。
- “等于”表示两个实例的值“相等”或“相同”，判定时要遵
  照设计者定义的评判标准，因此相对于“相等”来说，这是
  一种更加合适的叫法。

###类和结构体的选择
何时用类：

- 该数据结构的主要目的是用来封装少量相关简单数据值。
- 有理由预计该数据结构的实例在被赋值或传递时，封装的数据将会被拷贝而不是被引用。
- 该数据结构中储存的值类型属性，也应该被拷贝，而不是被引用。
- 该数据结构不需要去继承另一个既有类型的属性或者行为。

何时用结构体：

- 几何形状的大小，封装一个width属性和height属性，两者均为Double类型。
- 一定范围内的路径，封装一个start属性和length属性，两者均为Int类型。
- 三维坐标系内一点，封装x，y和z属性，三者均为Double类型。

###字符串、数组、和字典类型的赋值与复制行为
Swift 中，许多基本类型，诸如String，Array和Dictionary类型均以结构体的形式实现。这意味着被赋值给新的常量或变量，或者被传入函数或方法中时，它们的值会被拷贝。

Objective-C 中NSString，NSArray和NSDictionary类型均以类的形式实现，而并非结构体。它们在被赋值或者被传入函数或方法时，不会发生值拷贝，而是传递现有实例的引用。

###属性
###延迟存储属性
延迟存储属性是指当第一次被调用的时候才会计算其初始值的属性。在属性声明前使用 lazy 来标示一个延迟存储属性。

```
class DataManager {
    lazy var importer = DataImporter()
    var data = [String]()
    // 这里会提供数据管理功能
}

注意
必须将延迟存储属性声明成变量（使用 var 关键字），因为属性的初始值可能在实例构造完成之后才会得到。而常量属性在构造过程完成之前必须要有初始值，因此无法声明成延迟属性。

如果一个被标记为 lazy 的属性在没有初始化时就同时被多个线程访问，则无法保证该属性只会被初始化一次。
```

###计算属性
除存储属性外，类、结构体和枚举可以定义计算属性。计算属性不直接存储值，而是提供一个 getter 和一个可选的 setter，来间接获取和设置其他属性或变量的值。

```
struct Point {
    var x = 0.0, y = 0.0
}
struct Size {
    var width = 0.0, height = 0.0
}
struct Rect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) {
            origin.x = newCenter.x - (size.width / 2)
            origin.y = newCenter.y - (size.height / 2)
        }
    }
}
var square = Rect(origin: Point(x: 0.0, y: 0.0),
    size: Size(width: 10.0, height: 10.0))
let initialSquareCenter = square.center
square.center = Point(x: 15.0, y: 15.0)
print("square.origin is now at (\(square.origin.x), \(square.origin.y))")
// 打印 "square.origin is now at (10.0, 10.0)”
```

###简化Setter
如果计算属性的 setter 没有定义表示新值的参数名，则可以使用默认名称 newValue

```
struct AlternativeRect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set {
            origin.x = newValue.x - (size.width / 2)
            origin.y = newValue.y - (size.height / 2)
        }
    }
}
```

###只读计算属性
只有 getter 没有 setter 的计算属性就是只读计算属性。只读计算属性总是返回一个值，可以通过点运算符访问，但不能设置新的值。

只读计算属性的声明可以去掉 get 关键字和花括号：

```
struct Cuboid {
    var width = 0.0, height = 0.0, depth = 0.0
    var volume: Double {
        return width * height * depth
    }
}
let fourByFiveByTwo = Cuboid(width: 4.0, height: 5.0, depth: 2.0)
print("the volume of fourByFiveByTwo is \(fourByFiveByTwo.volume)")
// 打印 "the volume of fourByFiveByTwo is 40.0"
```

###属性观察器
- willSet 在新的值被设置之前调用
- didSet 在新的值被设置之后立即调用

```
注意
父类的属性在子类的构造器中被赋值时，它在父类中的 willSet 和 didSet 观察器会被调用，随后才会调用子类的观察器。在父类初始化方法调用之前，子类给属性赋值时，观察器不会被调用。 有关构造器代理的更多信息，请参考值类型的构造器代理和类的构造器代理规则。
```

```
class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newTotalSteps) {
            print("About to set totalSteps to \(newTotalSteps)")
        }
        didSet {
            if totalSteps > oldValue  {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}
let stepCounter = StepCounter()
stepCounter.totalSteps = 200
// About to set totalSteps to 200
// Added 200 steps
stepCounter.totalSteps = 360
// About to set totalSteps to 360
// Added 160 steps
stepCounter.totalSteps = 896
// About to set totalSteps to 896
// Added 536 steps
```

```
注意

如果将属性通过 in-out 方式传入函数，willSet 和 didSet 也会调用。这是因为 in-out 参数采用了拷入拷出模式：即在函数内部使用的是参数的 copy，函数结束后，又对参数重新赋值。
```

###全局变量和局部变量
计算属性和属性观察器所描述的功能也可以用于全局变量和局部变量。全局变量是在函数、方法、闭包或任何类型之外定义的变量。局部变量是在函数、方法或闭包内部定义的变量。

```
注意
全局的常量或变量都是延迟计算的，跟延迟存储属性相似，不同的地方在于，全局的常量或变量不需要标记lazy修饰符。
局部范围的常量或变量从不延迟计算。
```

###类型属性
实例属性属于一个特定类型的实例，每创建一个实例，实例都拥有属于自己的一套属性值，实例之间的属性相互独立。

也可以为类型本身定义属性，无论创建了多少个该类型的实例，这些属性都只有唯一一份。这种属性就是类型属性。

类型属性用于定义某个类型所有实例共享的数据，比如所有实例都能用的一个常量（就像 C 语言中的静态常量），或者所有实例都能访问的一个变量（就像 C 语言中的静态变量）。

存储型类型属性可以是变量或常量，计算型类型属性跟实例的计算型属性一样只能定义成变量属性

```
注意
跟实例的存储型属性不同，必须给存储型类型属性指定默认值，因为类型本身没有构造器，也就无法在初始化过程中使用构造器给类型属性赋值。
存储型类型属性是延迟初始化的，它们只有在第一次被访问的时候才会被初始化。即使它们被多个线程同时访问，系统也保证只会对其进行一次初始化，并且不需要对其使用 lazy 修饰符。
```

###类型属性语法
```
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}
enum SomeEnumeration {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 6
    }
}
class SomeClass {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    class var overrideableComputedTypeProperty: Int {
        return 107
    }
}

print(SomeStructure.storedTypeProperty)
// 打印 "Some value."
SomeStructure.storedTypeProperty = "Another value."
print(SomeStructure.storedTypeProperty)
// 打印 "Another value.”
print(SomeEnumeration.computedTypeProperty)
// 打印 "6"
print(SomeClass.computedTypeProperty)
// 打印 "27"
```

```
注意
例子中的计算型类型属性是只读的，但也可以定义可读可写的计算型类型属性，跟计算型实例属性的语法相同。
```
```
struct AudioChannel {
    static let thresholdLevel = 10
    static var maxInputLevelForAllChannels = 0
    var currentLevel: Int = 0 {
        didSet {
            if currentLevel > AudioChannel.thresholdLevel {
                // 将当前音量限制在阈值之内
                currentLevel = AudioChannel.thresholdLevel
            }
            if currentLevel > AudioChannel.maxInputLevelForAllChannels {
                // 存储当前音量作为新的最大输入音量
                AudioChannel.maxInputLevelForAllChannels = currentLevel
            }
        }
    }
}
```

```
注意
在第一个检查过程中，didSet 属性观察器将 currentLevel 设置成了不同的值，但这不会造成属性观察器被再次调用。
```



