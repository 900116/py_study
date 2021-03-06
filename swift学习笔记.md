## 基础部分  

### 整数的进制  

十进制：```let d = 17```<br>  
二进制：```let b = 0b00100```<br>  
八进制：```let o = 0o21```<br>  
十六进制: ```let h = 0x1a43```  

### typealias  

```typealias UID = UInt16```  

### 布尔  

```let x = true```  

### if  

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

### 元组

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

### 异常处理

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

### 断言
```
assert(age >= 0)
assert(age >= 0,"A person's age cannot be less than zero")
```

```
注意：
当代码使用优化编译的时候，断言将会被禁用，例如在 Xcode 中，使用默认的 target Release 配置
选项来 build 时，断言会被禁用。
```

## 运算符
### >= 和 <=
swift可以使用>=或者<=进行判断

```
1 >= 1   // true, 因为 1 大于等于 1
2 <= 1   // false, 因为 2 并不小于等于 1
```

### 元组的比较
元组大小会按照从左到右、逐值比较的方式，直到发现有两个值不等时停止。如果所有的值都相等，那么这一对元组我们就称它们是相等的。例如：

```
(1, "zebra") < (2, "apple")   // true，因为 1 小于 2
(3, "apple") < (3, "bird")    // true，因为 3 等于 3，但是 apple 小于 bird
(4, "dog") == (4, "dog")      // true，因为 4 等于 4，dog 等于 dog
```

### 空合运算符
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

### 区间运算符
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

## 字符与字符串
### 字符串常量

```
let someStr = "abcdef"
```

### 字符串支持+和+=操作
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

### 字符串是值类型
任何情况下，都会对已有字符串值创建新副本，并对该新副本进行传递或赋值操作。

### 使用字符
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

### 字符串插值
```
let multiplier = 3
let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"
```

```
注意：
插值字符串中写在括号中的表达式不能包含非转义反斜杠 (\)，并且不能包含回车或换行符。不过，插值字
符串可以包含其他字面量。
```

### Unicode标量
```
let dollarSign = "\u{24}"    // $, Unicode 标量 U+0024
let blackHeart = "\u{2665}"  // ♥, Unicode 标量 U+2665
let sparklingHeart = "\u{1F496}"// 💖, Unicode 标量U+1F496
```
### 计算字符数量
```
let unusualMenagerie = "Koala 🐨, Snail 🐌, Penguin 🐧, Dromedary 🐪"
print("unusualMenagerie has \(unusualMenagerie.characters.count) characters")
// 打印输出 "unusualMenagerie has 40 characters"
```

```
注意：
Swift 中的字符在一个字符串中并不一定占用相同的内存空间数量。如果您正在处理一个长字符串，需要注意characters属性必须遍历全部的 Unicode 标量，来确定字符串的字符数量。

characters.count并不总是等于NSString.length。NSString的length属性是利用 UTF-16 表示的十六位代码单元数字，而不是 Unicode 可扩展的字符群集。
```

### 字符串比较
字符串/字符可以用等于操作符(==)和不等于操作符(!=)表示值是否相等

```
注意：
在 Swift 中，字符串和字符并不区分地域。
```

### UTF-8表示
```
for codeUnit in dogString.utf8 {
    print("\(codeUnit) ", terminator: "")
}
print("")
// 68 111 103 226 128 188 240 159 144 182
```

### UTF-16表示
`dogString.utf16`

### Unicode 标量表示
您可以通过遍历String值的unicodeScalars属性来访问它的 Unicode 标量表示。 其为UnicodeScalarView类型的属性，UnicodeScalarView是UnicodeScalar类型的值的集合。
`dogString. unicodeScalars `

## 集合框架
### 三种集合类型
Swift 语言提供`Arrays`、`Sets`和`Dictionaries`三种基本的集合类型用来存储集合数据。

### 集合可变性
通过`let`和`var`区分是否可变

### 创建一个空数组
`var someInts = [Int]()`

### 创建一个带有默认值的数组
`var threeDoubles = Array(repeating: 0.0, count: 3)`

### 数组支持+和+=运算符
数组之间可以用`+`和`+=`方法

```
var arr_x = [1,2,3]
arr_x += [4,5]
```

### 判断数组为空
`isEmpty`可以判断数组是否为空，其等价于`count==0`

### 可以用区间批量改变数组的值
```
var arr_x = [1,2,3]
arr_x[1...2] = [10,10] //arr_x此时为[1,10,10]
```

### 用enumerated遍历数组
```
for (index, value) in shoppingList. enumerated() {
    print("Item \(String(index + 1)): \(value)")
}
```

### 创建和构造一个空的集合
`var letters = Set<Character>()`

### 可以用数组字面量创建一个集合
```
var favoriteGenres: Set<String> = ["Rock", "Classical", "Hip hop"]
```

### 集合操作
- `intersection(_:)`取交集。
- `symmetricDifference(_:)`取不同。
- `union(_:)`取并集。
- `subtracting(_:)`取差集。
- `==`相等。
- `isSubset(of:)`是否是子集(包含相等情况)。
- `isSuperset(of:)`是否是父集(包含相等情况)。
- `isStrictSubset(of:)`是否是子集(不包含相等情况)。
- `isStrictSuperset(of:)`是否是父集(不包含相等情况)。
- `isDisjoint(with:)`是否没有交集。

### 创建一个空字典
`var namesOfIntegers = [Int: String]()`

### 字典字面量
```
var airports: [String: String] = 
["YYZ": "Toronto Pearson", "DUB": "Dublin"]
```
### 字典遍历
```
for (airportCode, airportName) in airports {
    print("\(airportCode): \(airportName)")
}
```

## 控制流
### 使用匿名变量遍历
当你不需要知道下标的时候，你可以使用如下代码

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
### Repeat-While循环
Swift语言的`repeat-while`循环和其他语言中的`do-while`循环是类似的。

### 支持区间和组合的Switch
```
let x = 3
switch x {
case 0...4:
    print("hello")
case 5,6,7:
    print("hey")
default:
    print("what")
}
```
### Switch中的元组
我们可以使用元组在同一个switch语句中测试多个值。元组中的元素可以是值，也可以是区间。另外，使用下划线（_）来匹配所有可能的值。

```
let tup = (3,10)
switch tup {
case (0,0):
    print("must be (0,0)")
case (_,0):
    print("such as (1,0),(2,0),(3,0)")
case (3,_):
    print("such as (3,10),(3,2)")
case (5...7,2...8):
    print("such as (5,2),(6,8),(7,3)")
default:
    print("what")
}
```

### Switch值绑定与where
```
let lettup = (1,-1)
switch tup {
case let (x,y) where x == y:
    print("such as (1,1),(2,2)")
case let (x,_) where x > 0:
    print("such as (1,-1),(2,-8)")
default:
    print("other")
}
```

### Switch,For,Continue
```
let arr_ = [3,4,5,6,7]
for x in arr_ {
    switch x {
    case 5,7:
        continue
    default:
        print(x)
    }
}
```

### Switch贯穿
C语言中，你必须显示的调用`break`，才能跳过其他的分支，而Swift刚好与之相反，只要匹配到了一个分支，`switch`就结束了，你可以通过在分支下面加入`fallthrough`来实现C语言的`switch`

```
var result = 0.0
let intval = 66
switch intval {
case 91...100:
     result += Double(intval-90) * 1
     fallthrough
case 81...90:
    result += Double(intval-80) * 0.8
    fallthrough
case 71...80:
    result += Double(intval-70) * 0.6
    fallthrough
case 61...70:
    result += Double(intval-60) * 0.4
    fallthrough
case 0...60:
    result += Double(intval) * 0.2
    fallthrough
default:
     result += Double(intval) * 0.4
}
```

```
注意： fallthrough关键字不会检查它下一个将会落入执行的 case 中的匹配条件。fallthrough简单
地使代码继续连接到下一个 case 中的代码，这和 C 语言标准中的switch语句特性是一样的。
```

### Continue,Break的标签
当你有多层嵌套循环的时候，你可以用`continue/break label`来实现跳过指定的循环层

```
var counts = 0
externLoop : for i in 0...5 {
    for j in 0...6 {
        counts += 1
        if j == 1 && i < 3{
            continue externLoop
        }
        if j == 3 {
            break externLoop
        }
    }
}
//0,0   0,1   1,0   1,1   2,0  2,1   3,0  3,1   3,2   3,3
print(counts)  //count为10
```
### guard
不同于if语句，一个guard语句总是有一个else从句，如果条件不为真则执行else从句中的代码。(用于对允许值的过滤，往往不允许的值的条件，会让代码可读性变差，也有可能写漏)

```
func guard_func(obj:String?){
    guard let name = obj else {
        return
    }
    //数值合法，做处理
    print(obj)
}
guard_func(obj: nil)
guard_func(obj: "hey")
```

### #available
```
if #available(iOS 10, macOS 10.1,*) {
    //iOS10的新特性
}
```

## 函数
### 函数定义
```
func standard_func(name:String?,age:Int?) -> Bool{
    if let _ = name,let _ = age{
        return true
    }
    return false
}
func void_func(name:String){
    print("No Return Func")
}
func void_void_func(){
    print("No Params No Return Func")
}
func multi_return_func(arr:[Int]) -> (min:Int?,max:Int?){
    if arr.count == 0 {
        return (nil,nil)
    }
    if arr.count == 1 {
        return (arr[0],arr[1])
    }
    let max_value = arr.max(by: >)
    let min_value = arr.min(by: <)
    return (min_value,max_value)
}
```

### 可选元组返回类型
```
注意 可选元组类型如 (Int, Int)? 与元组包含可选类型如 (Int?, Int?) 是不同的.可选的元组类
型，整个元组是可选的，而不只是元组中的每个元素值。
```

### 指定参数标签
```
func greet(person: String, from hometown: String)
 -> String {
    return "Hello \(person)!  Glad you could visit from \(hometown)."
}
greet(person: "Bill", from: "Cupertino")
```

### 忽略参数标签
如果你不希望为某个参数添加一个标签，可以使用一个下划线(_)来代替一个明确的参数标签

```
func someFunction(_ firstParameterName: Int, secondParameterName: Int) {
     // 在函数体内，firstParameterName 和 secondParameterName 代表参数中的第一个和第二个参数值
}
someFunction(1, secondParameterName: 2)
```

### 模式参数值
将不带有默认值的参数放在函数参数列表的最前。一般来说，没有默认值的参数更加的重要，将不带默认值的参数放在最前保证在函数调用时，非默认参数的顺序是一致的，同时也使得相同的函数在不同情况下调用时显得更为清晰。

```
func default_vaule_func(name:String,greet:String = "Hello"){
    print("\(greet) \(name)")
}
default_vaule_func(name: "张三")
default_vaule_func(name: "李四", greet: "Hi")
```

### 可变参数
```
func avg_func(_ numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }
    return total / Double(numbers.count)
}
avg_func(1, 2, 3, 4, 5)

注意：
一个函数最多只能拥有一个可变参数。
```

### 输入输出参数
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

### 使用函数类型
```
var mathFunction: (Int, Int) -> Int = addTwoInts

func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Result: \(mathFunction(a, b))")
}

func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    return backward ? stepBackward : stepForward
}
```

### 嵌套函数
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

## 闭包
### 闭包表达式语法
```
reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```
### 根据上下文推断类型
如果`sorted(by:)`方法被一个字符串数组调用，其参数就必须是`(String, String) -> Bool`类型的函数。这意味着`(String, String)`和`Bool`可以省略。返回箭头`->`和围绕在参数周围的括号也可以被省略：

```
reversedNames = names.sorted(by: 
{ s1, s2 in return s1 > s2 } )
```

### 单表达式闭包隐式返回
单行表达式闭包可以通过省略`return`关键字来隐式返回单行表达式的结果。

```
reversedNames = names.sorted(by: { s1, s2 in s1 > s2 } )
```

### 参数名称缩写
swift 自动为内联闭包提供了参数名称缩写功能，你可以直接通过`$0`，`$1`，`$2` 来顺序调用闭包的参数，以此类推。

```
reversedNames = names.sorted(by: { $0 > $1 } )
```

### 运算符方法
实际上还有一种更简短的方式来编写上面例子中的闭包表达式。Swift 的`String`类型定义了关于大于号`>`的字符串实现，其作为一个函数接受两个`String`类型的参数并返回`Bool`类型的值。而这正好与 `sorted(by:)`方法的参数需要的函数类型相符合。

```
reversedNames = names.sorted(by: >)
```

### 尾随闭包
果你需要将一个很长的闭包表达式作为最后一个参数传递给函数，可以使用尾随闭包来增强函数的可读性

```
reversedNames = names.sorted() { $0 > $1 }
reversedNames = names.sorted { $0 > $1 }
```

### 闭包逃逸
当一个闭包作为参数传到一个函数中，但是这个闭包在函数返回之后才被执行，，你可以在参数名之前标注 @escaping，用来指明这个闭包是允许“逃逸”出这个函数的。

```
var c_arr = [() -> Void]()
func test_escape(closure:@escaping () -> Void) {
    c_arr.append(closure)
}
```
如果你不将这个参数标记为`@escaping`，就会得到一个编译错误。  
将一个闭包标记为`@escaping`意味着你必须在闭包中显式地引用`self`。

```
func test_no_escape(closure:() -> Void) {
    closure()
}

class SomeClass {
    var x = 10
    func doSomething() {
        test_escape { 
        self.x = 100 }
        test_no_escape { 
        x = 200 }
    }
}
```

### 自动闭包
这种闭包不接受任何参数，当它被调用的时候，会返回被包装在其中的表达式的值。你能够省略闭包的花括号，用一个普通的表达式来代闭包。这种闭包只需要在冒号后面添加`@autoclosure`

```
var customersInLine = ["Susan","Judy","Micheal"]
func serve(customer customerProvider: 
@autoclosure () -> String) { //自动闭包
    print("Now serving \(customerProvider())!")
}
serve(customer: customersInLine.remove(at: 0)) //不需要写大括号
//serve(customer: { customersInLine.remove(at: 0) } )  非自动闭包需要加大括号
```

```
注意 
过度使用 autoclosures 会让你的代码变得难以理解。上下文和函数名应该能够清晰地表明求值是
被延迟执行的。
```

如果你想让一个自动闭包可以“逃逸”，则应该同时使用`@autoclosure`和`@escaping`属性。

```
var customerProviders: [() -> String] = []
func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
    customerProviders.append(customerProvider)
}
collectCustomerProviders(customersInLine.remove(at: 0))
collectCustomerProviders(customersInLine.remove(at: 0))
```

## 枚举
### 枚举语法
```
enum CompassPoint {
    case north
    case south
    case east
    case west
}

var directionToHead = CompassPoint.west
directionToHead = .east
let directionToHead2:CompassPoint = .north
```

```
注意
Swift 的枚举成员在被创建时不会被赋予一个默认的整型值。这些枚举成员本身就是完备的值，这些值的类
型是已经明确定义好的CompassPoint类型。
```
当`directionToHead`的类型已知时，再次为其赋值可以省略枚举类型名。
###多个值可以出现在同一行
```
enum Planet {
    case mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
}
```

### 使用 Switch 语句匹配枚举值
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
switch语句必须穷举所有情况。如果忽略了.west这种情况，上面那段代码将无法通过编译。  
当不需要匹配每个枚举成员的时候，你可以提供一个default分支来涵盖所有未明确处理的枚举成员：

### 关联值
```
enum GoodsCode {
    case qrCode(String)
    case upc(Int,Int,Int,Int)
}

var code:GoodsCode = .upc(8, 8, 8, 8)
code = .qrCode("ABCDEF")

switch code {
case let .upc(a,b,c,d):
    print("\(a),\(b),\(c),\(d)")
case .qrCode(let codeStr):
    print(codeStr)
}
```

如果一个枚举成员的所有关联值都被提取为常量，你可以只在成员名称前标注一个let或者var

### 原始值
```
enum ASCIIControlCharacter: Character {
    case tab = "\t"
    case lineFeed = "\n"
    case carriageReturn = "\r"
}

注意
原始值和关联值是不同的。原始值是在定义枚举时被预先填充的值，像上述三个 ASCII 码。对于一个特定
的枚举成员，它的原始值始终不变。关联值是创建一个基于枚举成员的常量或变量时才设置的值，枚举成员
的关联值可以变化。
```

### 原始值的隐式赋值
```
enum Planet: Int {
    case mercury = 1, venus, earth, mars,
     jupiter, saturn, uranus, neptune
}

let earthsOrder = Planet.earth.rawValue
```

在上面的例子中，Plant.mercury的显式原始值为1，Planet.venus的隐式原始值为2，依次类推。


### 使用原始值初始化枚举实例
```
let possiblePlanet = Planet(rawValue: 7)
// possiblePlanet 类型为 Planet? 值为 Planet.uranus
// 如果原始值不存在则返回nil
```

### 递归枚举
递归枚举是一种枚举类型，它有一个或多个枚举成员使用该枚举类型的实例作为关联值。使用递归枚举时，编译器会插入一个间接层。你可以在枚举成员前加上indirect来表示该成员可递归。

```
enum MathExp {
    case number(Int)
    indirect case add(MathExp, MathExp)
    indirect case mul(MathExp, MathExp)
    indirect case sub(MathExp, MathExp)
    indirect case div(MathExp, MathExp)
}
```

你也可以在枚举类型开头加上`indirect`关键字来表明它的所有成员都是可递归的：

```
indirect enum MathExp {
    case number(Int)
    case addition(MathExp, MathExp)
    case multiplication(MathExp, MathExp)
}
```
例如，表达式(5 + 4) * 2，乘号右边是一个数字，左边则是另一个表达式。因为数据是嵌套的，因而用来存储数据的枚举类型也需要支持这种嵌套——这意味着枚举类型需要支持递归。

要操作具有递归性质的数据结构，使用递归函数是一种直截了当的方式。例如，下面是一个对算术表达式求值的函数：

```
func evaluate(_ expression: MathExp) -> Int {
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

## 类
### 类和结构体对比
共同点:  

- 定义属性  
- 定义方法  
- 定义下标  
- 定义构造器
- 定义扩展
- 实现协议  

类还有如下的附加功能：

- 可以继承
- 类型转换
- 析构器允许一个类实例释放任何其所被分配的资源
- 引用赋值

```
注意
结构体总是值传递，不存在引用计数。
```

### 定义语法
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

### 属性
Swift 允许直接设置结构体属性的子属性。不需要重新为整结构体设置新值。

### 结构体类型的成员逐一构造器
```
let vga = Resolution(width:640, height: 480)
```

### 结构体和枚举是值类型,类是引用类型
### 恒等运算符
- 等价于（`===`）
- 不等价于（`!==`）

```
f tenEighty === alsoTenEighty {
    print("tenEighty and alsoTenEighty refer to the same Resolution instance.")
}
//打印 "tenEighty and alsoTenEighty refer to the same Resolution instance."
```

请注意，“等价于”（用三个等号表示，`===`）与“等于”（用两个等号表示，`==`）的不同：

- “等价于”表示两个类对象（`class`）的地址相等。
- “等于”表示两个变量的值 (任何类型)“相等”或“相同”，判断逻辑可由开发者决定。

### 类和结构体的选择
何时用类：

- 该数据结构的主要目的是用来封装少量相关简单数据值。
- 有理由预计该数据结构的实例在被赋值或传递时，封装的数据将会被拷贝而不是被引用。
- 该数据结构中储存的值类型属性，也应该被拷贝，而不是被引用。
- 该数据结构不需要去继承另一个既有类型的属性或者行为。

何时用结构体：

- 几何形状的大小，封装一个`width`属性和`height`属性，两者均为`Double`类型。
- 一定范围内的路径，封装一个`start`属性和`length`属性，两者均为`Int`类型。
- 三维坐标系内一点，封装`x`，`y`和`z`属性，三者均为`Double`类型。

### 字符串、数组、和字典类型的赋值与复制行为
Swift 中，许多基本类型，诸如`String`，`Array`和`Dictionary`类型均以结构体的形式实现。它们都是值传递。而对应的OC中的类型(`NSString`等)都是类类型，通过引用传递。

### 属性
### 延迟存储属性
用`lazy`可以声明一个延迟特性的存储属性，延迟属性第一次调用才会付初值。

```
class DataManager {
    lazy var importer = DataImporter()
    var data = [String]()
    // 这里会提供数据管理功能
}

注意
延迟属性必须是变量(var),因为它赋值在构造之后。
lazy属于不是线程安全的。
```

### 计算属性
可以通过`getter`和`setter`为类，结构体和枚举定义计算属性。计算属性不存储值，而是通过`getter`，`setter`管理。

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
```

### 简化Setter
`setter`可以省略参数，使用默认名称 `newValue`s

```
set {
    origin.x = newValue.x - (size.width / 2)
    origin.y = newValue.y - (size.height / 2)
}
```

### 只读计算属性
只读计算属性，只有`getter`。它可以通过点运算符访问，但不能设置新的值。  
只读计算属性的声明可以去掉 `get` 关键字和花括号：

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

### 属性观察器
- `willSet` 在新的值被设置之前调用
- `didSet` 在新的值被设置之后立即调用

```
注意
父类的属性在子类的构造器中被赋值时，先调用父类观察器，后调用子类的观察器。在父类初始化方法调用之前(属性被赋值)，观察器不会被调用。
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
```

```
注意

如果将属性通过 in-out 方式传入函数，willSet 和 didSet 也会调用。这是因为 in-out 参数采用
了拷入拷出模式：即在函数内部使用的是参数的 copy，函数结束后，又对参数重新赋值。
```

### 全局变量和局部变量
全局变量和局部变量，都可以添加属性观察器。

```
注意
全局的常量或变量都是延迟计算的，不需要标记lazy修饰符。
局部范围的常量或变量从不延迟计算。
```

### 类属性
类属性，不论有多少个实例，属性都只有一份。  
它用于定义某个类型共享的数据。  
存储类属性可以是变量或常量，计算类属性只能定义成变量属性

```
注意
类属性必须给存储型类型属性指定默认值，因为类型本身没有构造器，所以无法使用构造器。
存储型类属性是延迟初始化的，它们只有在第一次被访问的时候才会被初始化，并且不需要对其使用 lazy 修饰符。
```

### 类型属性语法
类属性支持`struct` `enum` `class`

```
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}
```

```
注意
例子中的计算型类型属性是只读的，但也可以定义可读可写的计算型类型属性，跟计算型实例属性的语法相
同。
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
didSet中改变属性，不会造成死循环。
```

## 方法
### 在实例方法中修改值类型
结构体和枚举要想在方法中改变属性必须用`mutating`修饰（默认是不能改的，因为是值类型），在方法中甚至，可以改变self的值。

```
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveByX(deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
        //self = Point(x: x + deltaX, y: y + deltaY)
    }
}
```

### 类方法
通过`static`可以定义一个类方法。类还可以用关键字`class`来允许子类重写父类的方法实现。

```
注意
类、结构体、枚举都可以定义’类方法‘。
```

```
class SomeClass {
    class func someTypeMethod() {
        // 在这里实现类型方法
    }
}
SomeClass.someTypeMethod()
```

## 下标
### 定义下标属性
可以用`subscript`关键字来定义下标方法，下标还可以设定读写权限。

```
subscript(index: Int) -> Int {
    get {
      // 返回一个适当的 Int 类型的值
    }

    set(newValue) {
      // 执行适当的赋值操作
    }
}
```

### 下标选项
下标可以接受任意数量的入参，并且这些入参可以是任意类型，下标的返回值也可以是任意类型。  
下标可以使用变量参数和可变参数，但不能使用输入输出参数，也不能给参数设置默认值。  
类或结构体可以提供多个下标实现并且支持重载。   
重写`indexIsValidForRow`方法可以判断下标是否合法。  

```
struct Matrix {
    let rows: Int, columns: Int
    var grid: [Double]
    init(rows: Int, columns: Int) {
        self.rows = rows
        self.columns = columns
        grid = Array(count: rows * columns, repeatedValue: 0.0)
    }
    func indexIsValidForRow(row: Int, column: Int) -> Bool {
        return row >= 0 && row < rows && column >= 0 && column < columns
    }
    subscript(row: Int, column: Int) -> Double {
        get {
            assert(indexIsValidForRow(row, column: column), "Index out of range")
            return grid[(row * columns) + column]
        }
        set {
            assert(indexIsValidForRow(row, column: column), "Index out of range")
            grid[(row * columns) + column] = newValue
        }
    }
}
```

## 继承
### 继承语法
```
class Bicycle: Vehicle {
    var hasBasket = false
}
```

### 重写
可以重写继承来的实例方法，类方法，实例属性，或下标提供自己定制的实现。

如果要重写，需要加上`override`关键字。  
任何缺少`override`关键字的重写都会在编译时被诊断为错误。

### super
在合适的地方，你可以通过使用`super`前缀来调用父类的方法，属性或下标：

- `super.someMethod()`调用父类方法
- `super.someProperty`调用父类属性
- `super[someIndex]`调用父类的下标方法

### 重写属性
你可以重写继承来的实例属性或类属性，提供自己定制的`getter`和`setter`,`willSet`,`didSet`。

重写一个属性时，必需将它的名字和类型都写出来。

你可以将一个继承来的只读属性重写为一个读写属性。但是，你不可以将一个继承来的读写属性重写为一个只读属性。

```
class Car: Vehicle {
    var gear = 1
    override var description: String {
        return super.description + " in gear \(gear)"
    }
}
```

```
注意
如果你在重写属性中提供了 setter，那么你也一定要提供 getter。如果你不想在重写版本中
的 getter 里修改继承来的属性值，你可以直接通过super.someProperty来返回继承来的值，
其中someProperty是你要重写的属性的名字。
```

你可以通过重写属性为一个继承来的属性添加属性观察器。

```
注意
你不可以为继承来的常量存储型属性或继承来的只读计算型属性添加属性观察器。这些属性的值是不可以被设
置的，所以，为它们提供willSet或didSet实现是不恰当。  
你不可以同时提供重写的 setter 和重写的属性观察器。你可以在setter中实现属性观察的效果。
```

```
class AutomaticCar: Car {
    override var currentSpeed: Double {
        didSet {
            gear = Int(currentSpeed / 10.0) + 1
        }
    }
}
```

### 防止重写
通过`final`关键字防止方法，属性或下标被重写（例如：`final var`，`final func`，`final class func`，以及`final subscript`）。

重写`final`属性或下标，在编译时会报错。

通过`final`在关键字防止类被继承，试图继承这样的类会导致编译报错。


## 构造过程
### 存储属性的初始赋值
类和结构体在创建实例时，必须为所有存储型属性设置合适的初始值。存储型属性的值不能处于一个未知的状态。

你可以在构造器中为存储型属性赋初值，也可以在定义属性时为其设置默认值。

```
注意
当你为存储型属性设置默认值或者在构造器中为其赋值时，它们的值是被直接设置的，不会触发任何属性观察
者。
```

### 构造器
```
init() {
    // 在此处执行构造过程
}
```

### 参数的内部名称和外部名称
跟函数和方法参数相同，构造参数也拥有一个在构造器内部使用的参数名字和一个在调用构造器时使用的外部参数名字。

```
struct Color {
    let red, green, blue: Double
    init(red: Double, green: Double, blue: Double) {
        self.red   = red
        self.green = green
        self.blue  = blue
    }
    init(white: Double) {
        red   = white
        green = white
        blue  = white
    }
}
```
注意，如果不通过外部参数名字传值，你是没法调用这个构造器的。只要构造器定义了某个外部参数名，你就必须使用它，忽略它将导致编译错误：

```
// 报编译时错误，需要外部名称
let veryGreen = Color(0.0, 1.0, 0.0)
```

### 不带外部名的构造器参数
你可以使用下划线(_)来省略参数的外部名，以此重写上面所说的默认行为。

```
struct Celsius {
    var temperatureInCelsius: Double
    init(fromFahrenheit fahrenheit: Double) {
        temperatureInCelsius = (fahrenheit - 32.0) / 1.8
    }
    init(fromKelvin kelvin: Double) {
        temperatureInCelsius = kelvin - 273.15
    }
    init(_ celsius: Double){
        temperatureInCelsius = celsius
    }
}
let bodyTemperature = Celsius(37.0)
// bodyTemperature.temperatureInCelsius 为 37.0
```

### 构造过程中常量属性的修改
你可以在构造过程中的任意时间点给常量属性指定一个值，只要在构造过程结束时是一个确定的值。一旦常量属性被赋值，它将永远不可更改。

```
注意
对于类的实例来说，它的常量属性只能在定义它的类的构造过程中修改；不能在子类中修改。
```

### 默认构造器
如果结构体或类的所有属性都有默认值，同时没有自定义的构造器，那么 Swift 会给这些结构体或类提供一个默认构造器（`default initializers`）。这个默认构造器将简单地创建一个所有属性值都设置为默认值的实例。

```
class ShoppingListItem {
    var name: String?
    var quantity = 1
    var purchased = false
}
var item = ShoppingListItem()
```

尽管代码中没有显式为name属性设置默认值，但由于name是可选字符串类型，它将默认设置为nil

### 结构体的逐一成员构造器
除了上面提到的默认构造器，如果结构体没有提供自定义的构造器，它们将自动获得一个逐一成员构造器，即使结构体的存储型属性没有默认值。

```
struct Size {
    var width = 0.0, height = 0.0
}
let twoByTwo = Size(width: 2.0, height: 2.0)
```

### 值类型的构造器代理
构造器可以通过调用其它构造器来完成实例的部分构造过程。这一过程称为构造器代理，它能减少多个构造器间的代码重复。

```
struct Rect {
    var origin = Point()
    var size = Size()
    init() {}
    init(origin: Point, size: Size) {
        self.origin = origin
        self.size = size
    }
    init(center: Point, size: Size) {
        let originX = center.x - (size.width / 2)
        let originY = center.y - (size.height / 2)
        self.init(origin: Point(x: originX, y: originY), size: size)
    }
}
```

如果你为某个值类型定义了一个自定义的构造器，你将无法访问到默认构造器（如果是结构体，还将无法访问逐一成员构造器）。这种限制可以防止你为值类型增加了一个额外的且十分复杂的构造器之后,仍然有人错误的使用自动生成的构造器

```
注意
假如你希望默认构造器、逐一成员构造器以及你自己的自定义构造器都能用来创建实例，可以将自定义的构造
器写到扩展（extension）中，而不是写在值类型的原始定义中。想查看更多内容，请查看扩展章节。
```

```
注意
如果你想用另外一种不需要自己定义init()和init(origin:size:)的方式来实现这个例子，请参考扩展。

```

### 类的继承和构造过程
类里面的所有存储型属性——包括所有继承自父类的属性——都必须在构造过程中设置初始值。

### 指定构造器和便利构造器
指定构造器是类中最主要的构造器。一个指定构造器将初始化类中提供的所有属性，并根据父类链往上调用父类的构造器来实现父类的初始化。

每一个类都必须拥有至少一个指定构造器。在某些情况下，许多类通过继承了父类中的指定构造器而满足了这个条件。

便利构造器是类中比较次要的、辅助型的构造器。你可以定义便利构造器来调用同一个类中的指定构造器，并为其参数提供默认值。你也可以定义便利构造器来创建一个特殊用途或特定输入值的实例。

```
init(parameters) {
    statements
}

//便利构造器也采用相同样式的写法，但需要在init关键字之前放置convenience关键字，
并使用空格将它们俩分开：

convenience init(parameters) {
    statements
}
```

### 类的构造器代理规则
规则 1

指定构造器必须调用其直接父类的的指定构造器。

规则 2

便利构造器必须调用同类中定义的其它构造器。

规则 3

便利构造器必须最终导致一个指定构造器被调用。

一个更方便记忆的方法是：

- 指定构造器必须总是向上代理
- 便利构造器必须总是横向代理

```
注意
这些规则不会影响类的实例如何创建。任何上图中展示的构造器都可以用来创建完全初始化的实例。这些规则
只影响类定义如何实现。
```

### 两段式构造过程
- 每个存储型属性被引入它们的类指定一个初始值。当每个存储型属性的初始值被确定后。
- 它给每个类一次机会，在新实例准备使用之前进一步定制它们的存储型属性。

```
注意
Swift 的两段式构造过程跟 Objective-C 中的构造过程类似。最主要的区别在于阶段 1，Objective-C 
给每一个属性赋值0或空值（比如说0或nil）。Swift 的构造流程则更加灵活，它允许你设置定制的初始
值，并自如应对某些属性不能以0或nil作为合法默认值的情况。
```

安全检查 1

指定构造器必须保证它所在类引入的所有属性都必须先初始化完成，之后才能将其它构造任务向上代理给父类中的构造器。

如上所述，一个对象的内存只有在其所有存储型属性确定之后才能完全初始化。为了满足这一规则，指定构造器必须保证它所在类引入的属性在它往上代理之前先完成初始化。

安全检查 2

指定构造器必须先向上代理调用父类构造器，然后再为继承的属性设置新值。如果没这么做，指定构造器赋予的新值将被父类中的构造器所覆盖。

安全检查 3

便利构造器必须先代理调用同一类中的其它构造器，然后再为任意属性赋新值。如果没这么做，便利构造器赋予的新值将被同一类中其它指定构造器所覆盖。

安全检查 4

构造器在第一阶段构造完成之前，不能调用任何实例方法，不能读取任何实例属性的值，不能引用self作为一个值。

类实例在第一阶段结束以前并不是完全有效的。只有第一阶段完成后，该实例才会成为有效实例，才能访问属性和调用方法。


阶段 1

- 某个指定构造器或便利构造器被调用。
- 完成新实例内存的分配，但此时内存还没有被初始化。
- 指定构造器确保其所在类引入的所有存储型属性都已赋初值。存储型属性所属的内存完成初始化。
- 指定构造器将调用父类的构造器，完成父类属性的初始化。
- 这个调用父类构造器的过程沿着构造器链一直往上执行，直到到达构造器链的最顶部。
- 当到达了构造器链最顶部，且已确保所有实例包含的存储型属性都已经赋值，这个实例的内存被认为已经完全初始化。此时阶段 1 完成。

阶段 2

- 从顶部构造器链一直往下，每个构造器链中类的指定构造器都有机会进一步定制实例。构造器此时可以访问self、修改它的属性并调用实例方法等等。
- 最终，任意构造器链中的便利构造器可以有机会定制实例和使用self。

### 构造器的继承和重写
跟 Objective-C 中的子类不同，Swift 中的子类默认情况下不会继承父类的构造器。Swift 的这种机制可以防止一个父类的简单构造器被一个更精细的子类继承，并被错误地用来创建子类的实例。

```
注意
父类的构造器仅会在安全和适当的情况下被继承。
```

假如你希望自定义的子类中能提供一个或多个跟父类相同的构造器，你可以在子类中提供这些构造器的自定义实现。

```
注意
当你重写一个父类的指定构造器时，你总是需要写override修饰符，即使你的子类将父类的指定构造器重写
为了便利构造器。
```

相反，如果你编写了一个和父类便利构造器相匹配的子类构造器，由于子类不能直接调用父类的便利构造器（每个规则都在上文类的构造器代理规则有所描述），因此，严格意义上来讲，你的子类并未对一个父类构造器提供重写。最后的结果就是，你在子类中“重写”一个父类便利构造器时，不需要加override前缀。

```
class Vehicle {
    var numberOfWheels = 0
    var description: String {
        return "\(numberOfWheels) wheel(s)"
    }
}

class Bicycle: Vehicle {
    override init() {
        super.init()
        numberOfWheels = 2
    }
}
```


```
注意
子类可以在初始化时修改继承来的变量属性，但是不能修改继承来的常量属性。
```

### 构造器的自动继承
如上所述，子类在默认情况下不会继承父类的构造器。但是如果满足特定条件，父类构造器是可以被自动继承的。

规则 1

如果子类没有定义任何指定构造器，它将自动继承所有父类的指定构造器。

规则 2

如果子类提供了所有父类指定构造器的实现——无论是通过规则 1 继承过来的，还是提供了自定义实现——它将自动继承所有父类的便利构造器。

即使你在子类中添加了更多的便利构造器，这两条规则仍然适用。

```
注意
对于规则 2，子类可以将父类的指定构造器实现为便利构造器。
```

### 可失败构造器
如果一个类、结构体或枚举类型的对象，在构造过程中有可能失败，则为其定义一个可失败构造器。这里所指的“失败”是指，如给构造器传入无效的参数值，或缺少某种所需的外部资源，又或是不满足某种必要的条件等。

其语法为在init关键字后面添加问号(init?)。


```
注意
可失败构造器的参数名和参数类型，不能与其它非可失败构造器的参数名，及其参数类型相同。
```

可失败构造器会创建一个类型为自身类型的可选类型的对象。你通过return nil语句来表明可失败构造器在何种情况下应该“失败”。

```
注意
严格来说，构造器都不支持返回值。因为构造器本身的作用，只是为了确保对象能被正确构造。因此你只是用return nil表明可失败构造器构造失败，而不要用关键字return来表明构造成功。
```

```
struct Animal {
    let species: String
    init?(species: String) {
        if species.isEmpty { return nil }
        self.species = species
    }
}
```

### 枚举类型的可失败构造器
```
enum TemperatureUnit {
    case Kelvin, Celsius, Fahrenheit
    init?(symbol: Character) {
        switch symbol {
        case "K":
            self = .Kelvin
        case "C":
            self = .Celsius
        case "F":
            self = .Fahrenheit
        default:
            return nil
        }
    }
}
```

### 带原始值的枚举类型的可失败构造器
带原始值的枚举类型会自带一个可失败构造器init?(rawValue:)，该可失败构造器有一个名为rawValue的参数，其类型和枚举类型的原始值类型一致，如果该参数的值能够和某个枚举成员的原始值匹配，则该构造器会构造相应的枚举成员，否则构造失败。

```
enum TemperatureUnit: Character {
    case Kelvin = "K", Celsius = "C", Fahrenheit = "F"
}

let unknownUnit = TemperatureUnit(rawValue: "X")
if unknownUnit == nil {
    print("This is not a defined temperature unit, so initialization failed.")
}
```

### 构造失败的传递
可失败构造器可以横向或者纵向代理。

无论是向上代理还是横向代理，如果你代理到的其他可失败构造器触发构造失败，整个构造过程将立即终止，接下来的任何构造代码不会再被执行。

```
注意
可失败构造器也可以代理到其它的非可失败构造器。通过这种方式，你可以增加一个可能的失败状态到现有的
构造过程中。
```

### 重写一个可失败构造器
如同其它的构造器，你可以在子类中重写父类的可失败构造器。或者你也可以用子类的非可失败构造器重写一个父类的可失败构造器。这使你可以定义一个不会构造失败的子类，即使父类的构造器允许构造失败。

注意，当你用子类的非可失败构造器重写父类的可失败构造器时，向上代理到父类的可失败构造器的唯一方式是对父类的可失败构造器的返回值进行强制解包。

```
注意
你可以用非可失败构造器重写可失败构造器，但反过来却不行。
```

```
class Document {
    var name: String?
    // 该构造器创建了一个 name 属性的值为 nil 的 document 实例
    init() {}
    // 该构造器创建了一个 name 属性的值为非空字符串的 document 实例
    init?(name: String) {
        self.name = name
        if name.isEmpty { return nil }
    }
}

class AutomaticallyNamedDocument: Document {
    override init() {
        super.init()
        self.name = "[Untitled]"
    }
    override init(name: String) {
        super.init()
        if name.isEmpty {
            self.name = "[Untitled]"
        } else {
            self.name = name
        }
    }
}
```
你可以在子类的非可失败构造器中使用强制解包来调用父类的可失败构造器。

```
class UntitledDocument: Document {
    override init() {
        super.init(name: "[Untitled]")!
    }
}
```

### init!

通常来说我们通过在init关键字后添加问号的方式（init?）来定义一个可失败构造器，但你也可以通过在init后面添加惊叹号的方式来定义一个可失败构造器（init!），该可失败构造器将会构建一个对应类型的隐式解包可选类型的对象。

你可以在init?中代理到init!，反之亦然。你也可以用init?重写init!，反之亦然。你还可以用init代理到init!，不过，一旦init!构造失败，则会触发一个断言。

### 必要构造器
在类的构造器前添加required修饰符表明所有该类的子类都必须实现该构造器

```
class SomeClass {
    required init() {
        // 构造器的实现代码
    }
}
```

在子类重写父类的必要构造器时，必须在子类的构造器前也添加required修饰符，表明该构造器要求也应用于继承链后面的子类。在重写父类中必要的指定构造器时，不需要添加override修饰符：

```
class SomeSubclass: SomeClass {
    required init() {
        // 构造器的实现代码
    }
}
```

```
注意
如果子类继承的构造器能满足必要构造器的要求，则无须在子类中显式提供必要构造器的实现。
```

### 通过闭包或函数设置属性的默认值
```
class SomeClass {
    let someProperty: SomeType = {
        // 在这个闭包中给 someProperty 创建一个默认值
        // someValue 必须和 SomeType 类型相同
        return someValue
    }()
}
```

```
注意
如果你使用闭包来初始化属性，请记住在闭包执行时，实例的其它部分都还没有初始化。这意味着你不能在闭
包里访问其它属性，即使这些属性有默认值。同样，你也不能使用隐式的self属性，或者调用任何实例方法。
```

## 析构过程
### 析构语法

```
deinit {
    // 执行析构过程
}
```

## 自动引用计数
### weak

```
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    weak var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```

```
注意
当 ARC 设置弱引用为nil时，属性观察不会被触发。
```

```
注意
在使用垃圾收集的系统里，弱指针有时用来实现简单的缓冲机制，因为没有强引用的对象只会在内存压力触发
垃圾收集时才被销毁。但是在 ARC 中，一旦值的最后一个强引用被移除，就会被立即销毁，这导致弱引用并
不适合上面的用途。
```

### 无主引用
和弱引用类似，无主引用不会牢牢保持住引用的实例。和弱引用不同的是，无主引用在其他实例有相同或者更长的生命周期时使用。你可以在声明属性或者变量时，在前面加上关键字unowned表示这是一个无主引用。

```
重要
使用无主引用，你必须确保引用始终指向一个未销毁的实例。
如果你试图在实例被销毁后，访问该实例的无主引用，会触发运行时错误。
```

由于信用卡总是关联着一个客户，因此将customer属性定义为无主引用，用以避免循环强引用：

```
class Customer {
    let name: String
    var card: CreditCard?
    init(name: String) {
        self.name = name
    }
    deinit { print("\(name) is being deinitialized") }
}

class CreditCard {
    let number: UInt64
    unowned let customer: Customer
    init(number: UInt64, customer: Customer) {
        self.number = number
        self.customer = customer
    }
    deinit { print("Card #\(number) is being deinitialized") }
}
```

```
注意
上面的例子展示了如何使用安全的无主引用。对于需要禁用运行时的安全检查的情况（例如，出于性能方面的
原因），Swift还提供了不安全的无主引用。与所有不安全的操作一样，你需要负责检查代码以确保其安全
性。 你可以通过unowned(unsafe)来声明不安全无主引用。如果你试图在实例被销毁后，访问该实例的不
安全无主引用，你的程序会尝试访问该实例之前所在的内存地址，这是一个不安全的操作。
```

### 无主引用以及隐式解析可选属性
Person和Apartment的例子展示了两个属性的值都允许为nil，并会潜在的产生循环强引用。这种场景最适合用弱引用来解决。

Customer和CreditCard的例子展示了一个属性的值允许为nil，而另一个属性的值不允许为nil，这也可能会产生循环强引用。这种场景最适合通过无主引用来解决。

然而，存在着第三种场景，在这种场景中，两个属性都必须有值，并且初始化完成后永远不会为nil。在这种场景中，需要一个类使用无主属性，而另外一个类使用隐式解析可选属性。

```
class Country {
    let name: String
    var capitalCity: City!
    init(name: String, capitalName: String) {
        self.name = name
        self.capitalCity = City(name: capitalName, country: self)
    }
}

class City {
    let name: String
    unowned let country: Country
    init(name: String, country: Country) {
        self.name = name
        self.country = country
    }
}
```

### 闭包引起的循环强引用
```
lass HTMLElement {

    let name: String
    let text: String?

    lazy var asHTML: Void -> String = {
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }

    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }

    deinit {
        print("\(name) is being deinitialized")
    }

}
```

```
注意
asHTML声明为lazy属性，因为只有当元素确实需要被处理为 HTML 输出的字符串时，才需要使用asHTML。
也就是说，在默认的闭包中可以使用self，因为只有当初始化完成以及self确实存在后，才能访问lazy属
性。
```

```
注意
虽然闭包多次使用了self，它只捕获HTMLElement实例的一个强引用。
```

### 解决闭包引起的循环强引用

在定义闭包时同时定义捕获列表作为闭包的一部分，通过这种方式可以解决闭包和类实例之间的循环强引用。捕获列表定义了闭包体内捕获一个或者多个引用类型的规则。跟解决两个类实例间的循环强引用一样，声明每个捕获的引用为弱引用或无主引用，而不是强引用。应当根据代码关系来决定使用弱引用还是无主引用。

```
注意
Swift 有如下要求：只要在闭包内使用self的成员，就要用self.someProperty或者
self.someMethod()（而不只是someProperty或someMethod()）。这提醒你可能会一不小心就捕获了
self。
```


### 定义捕获列表
```
lazy var someClosure: (Int, String) -> String = {
    [unowned self, weak delegate = self.delegate!] (index: Int, stringToProcess: String) -> String in
    // 这里是闭包的函数体
}
```

如果闭包没有指明参数列表或者返回类型，即它们会通过上下文推断，那么可以把捕获列表和关键字in放在闭包最开始的地方：

```
lazy var someClosure: Void -> String = {
    [unowned self, weak delegate = self.delegate!] in
    // 这里是闭包的函数体
}
```

在闭包和捕获的实例总是互相引用并且总是同时销毁时，将闭包内的捕获定义为无主引用。

```
注意
如果被捕获的引用绝对不会变为nil，应该用无主引用，而不是弱引用。
```

## 可选链式调用
```
注意
Swift 的可选链式调用和 Objective-C 中向nil发送消息有些相像，但是 Swift 的可选链式调用可以应
用于任意类型，并且能检查调用是否成功。
```
### 使用可选链式调用代替强制展开
通过在想调用的属性、方法、或下标的可选值后面放一个问号（?），可以定义一个可选链。这一点很像在可选值后面放一个叹号（!）来强制展开它的值。它们的主要区别在于当可选值为空时可选链式调用只会调用失败，然而强制展开将会触发运行时错误。

```
let roomCount = john.residence!.numberOfRooms
// 这会引发运行时错误

if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else {
    print("Unable to retrieve the number of rooms.")
}
// 打印 “Unable to retrieve the number of rooms.”
```

### 通过可选链式调用访问下标
```
注意
通过可选链式调用访问可选值的下标时，应该将问号放在下标方括号的前面而不是后面。可选链式调用的问号
一般直接跟在可选表达式的后面。
```

```
john.residence?[0] = Room(name: "Bathroom")
```

### 访问可选类型的下标
如果下标返回可选类型值，比如 Swift 中Dictionary类型的键的下标，可以在下标的结尾括号后面放一个问号来在其可选返回值上进行可选链式调用

```
var testScores = ["Dave": [86, 82, 84], "Bev": [79, 94, 81]]
testScores["Dave"]?[0] = 91
testScores["Bev"]?[0] += 1
testScores["Brian"]?[0] = 72
// "Dave" 数组现在是 [91, 82, 84]，"Bev" 数组现在是 [80, 94, 81]
```

### 连接多层可选链式调用
可以通过连接多个可选链式调用在更深的模型层级中访问属性、方法以及下标。然而，多层可选链式调用不会增加返回值的可选层级。

也就是说：

- 如果你访问的值不是可选的，可选链式调用将会返回可选值。
- 如果你访问的值就是可选的，可选链式调用不会让可选返回值变得“更可选”。

因此：

- 通过可选链式调用访问一个Int值，将会返回Int?，无论使用了多少层可选链式调用。
- 类似的，通过可选链式调用访问Int?值，依旧会返回Int?值，并不会返回Int??。

### 在方法的可选返回值上进行可选链式调用
```
if let beginsWithThe =
    john.residence?.address?.buildingIdentifier()?.hasPrefix("The") {
        if beginsWithThe {
            print("John's building identifier begins with \"The\".")
        } else {
            print("John's building identifier does not begin with \"The\".")
        }
}
```

```
注意
在上面的例子中，在方法的圆括号后面加上问号是因为你要在buildingIdentifier()方法的可选返回值上
进行可选链式调用，而不是方法本身。
```

## 异常处理
### throw
```
enum VendingMachineError: Error {
    case invalidSelection                    //选择无效
    case insufficientFunds(coinsNeeded: Int) //金额不足
    case outOfStock                          //缺货
}

throw VendingMachineError. insufficientFunds(coinsNeeded: 5)
```

### 处理错误
swift 中有4种处理错误的方式。

- 函数抛出错误
- do - catch
- 将错误进行可选处理
- 或者用断言避免此种错误

在调用一个能抛出错误的函数、方法或者构造器之前，加上try关键字，或者try?或try!这种变体。

```
注意
Swift 中的错误处理和其他语言中用try，catch和throw进行异常处理很像。和其他语言中（包括 
Objective-C ）的异常处理不同的是，Swift 中的错误处理并不涉及解除调用栈，这是一个计算代价高昂
的过程。就此而言，throw语句的性能特性是可以和return语句相媲美的。
```  

### 用 throwing 函数传递错误
为了表示一个函数、方法或构造器可以抛出错误，在函数声明的参数列表之后加上throws关键字。一个标有throws关键字的函数被称作throwing 函数。如果这个函数指明了返回值类型，throws关键词需要写在箭头（->）的前面。

```
func canThrowErrors() throws -> String
func cannotThrowErrors() -> String
```

```
注意
只有 throwing 函数可以传递错误。任何在某个非 throwing 函数内部抛出的错误只能在函数内部处理。
```

### 用Do - Catch处理错误
```
do {
    try expression
    statements
} catch pattern 1 {
    statements
} catch pattern 2 where condition {
    statements
}
```

### 将错误转换成可选值
可以使用try?通过将错误转换成一个可选值来处理错误。如果在评估try?表达式时一个错误被抛出，那么表达式的值就是nil。

```
func someThrowingFunction() throws -> Int {
    // ...
}

let x = try? someThrowingFunction()

let y: Int?
do {
    y = try someThrowingFunction()
} catch {
    y = nil
}

func fetchData() -> Data? {
    if let data = try? fetchDataFromDisk() { return data }
    if let data = try? fetchDataFromServer() { return data }
    return nil
}
```

### 禁用错误传递
有时你知道某个throwing函数实际上在运行时是不会抛出错误的，在这种情况下，你可以在表达式前面写try!来禁用错误传递，这会把调用包装在一个不会有错误抛出的运行时断言中。如果真的抛出了错误，你会得到一个运行时错误。

```
let photo = try! loadImage(atPath: "./Resources/John Appleseed.jpg")
```

### defer
可以使用defer语句在即将离开当前代码块时执行一系列语句。该语句让你能执行一些必要的清理工作，不管是以何种方式离开当前代码块的——无论是由于抛出错误而离开，还是由于诸如return或者break的语句。

defer语句将代码的执行延迟到当前的作用域退出之前。

```
func processFile(filename: String) throws {
    if exists(filename) {
        let file = open(filename)
        defer {
            close(file)
        }
        while let line = try file.readline() {
            // 处理文件。
        }
        // close(file) 会在这里被调用，即作用域的最后。
    }
}
```

```
注意
即使没有涉及到错误处理，你也可以使用defer语句。
```

## 类型转换
### as? 和 as!
某类型的一个常量或变量可能在幕后实际上属于一个子类。当确定是这种情况时，你可以尝试向下转到它的子类型，用类型转换操作符（as? 或 as!）。

因为向下转型可能会失败，类型转型操作符带有两种不同形式。条件形式as? 返回一个你试图向下转成的类型的可选值。强制形式 as! 把试图向下转型和强制解包（转换结果结合为一个操作。

当你不确定向下转型可以成功时，用类型转换的条件形式（as?）。条件形式的类型转换总是返回一个可选值，并且若下转是不可能的，可选值将是 nil。这使你能够检查向下转型是否成功。

```
注意
转换没有真的改变实例或它的值。根本的实例保持不变；只是简单地把它作为它被转换成的类型来使用。
```

### Any 和 AnyObject 的类型转换
Swift 为不确定类型提供了两种特殊的类型别名：

- Any 可以表示任何类型，包括函数类型。
- AnyObject 可以表示任何类类型的实例。

```
注意
Any类型可以表示所有类型的值，包括可选类型。Swift 会在你用Any类型来表示一个可选值的时候，给你一
个警告。如果你确实想使用Any类型来承载可选值，你可以使用as操作符显式转换为Any，如下所示：

let optionalNumber: Int? = 3
things.append(optionalNumber)        // 警告
things.append(optionalNumber as Any) // 没有警告
```

## 嵌套类型
### 嵌套类型实践
```
struct BlackjackCard {
    // 嵌套的 Suit 枚举
    enum Suit: Character {
       case Spades = "♠", Hearts = "♡", Diamonds = "♢", Clubs = "♣"
    }

    // 嵌套的 Rank 枚举
    enum Rank: Int {
       case Two = 2, Three, Four, Five, Six, Seven, Eight, Nine, Ten
       case Jack, Queen, King, Ace
       struct Values {
           let first: Int, second: Int?
       }
       var values: Values {
        switch self {
        case .Ace:
            return Values(first: 1, second: 11)
        case .Jack, .Queen, .King:
            return Values(first: 10, second: nil)
        default:
            return Values(first: self.rawValue, second: nil)
            }
       }
    }

    // BlackjackCard 的属性和方法
    let rank: Rank, suit: Suit
    var description: String {
        var output = "suit is \(suit.rawValue),"
        output += " value is \(rank.values.first)"
        if let second = rank.values.second {
            output += " or \(second)"
        }
        return output
    }
}


let heartsSymbol = BlackjackCard.Suit.Hearts.rawValue
// 红心符号为 “♡”
```

## 扩展
### 扩展语法
```
extension SomeType {
    // 为 SomeType 添加的新功能写到这里
}

extension SomeType: SomeProtocol, AnotherProctocol {
    // 协议实现写到这里
}
```

```
注意
如果你通过扩展为一个已有类型添加新功能，那么新功能对该类型的所有已有实例都是可用的，即使它们是在
这个扩展定义之前创建的。
```

### 计算型属性
扩展可以为已有类型添加计算型实例属性和计算型类型属性。

```
extension Double {
    var km: Double { return self * 1_000.0 }
    var m : Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
let oneInch = 25.4.mm
print("One inch is \(oneInch) meters")
// 打印 “One inch is 0.0254 meters”
let threeFeet = 3.ft
print("Three feet is \(threeFeet) meters")
// 打印 “Three feet is 0.914399970739201 meters”
```

```
注意
扩展可以添加新的计算型属性，但是不可以添加存储型属性，也不可以为已有属性添加属性观察器。
```

### 构造器
```
注意
如果你使用扩展为一个值类型添加构造器，同时该值类型的原始实现中未定义任何定制的构造器且所有存储属
性提供了默认值，那么我们就可以在扩展中的构造器里调用默认构造器和逐一成员构造器。
正如在值类型的构造器代理中描述的，如果你把定制的构造器写在值类型的原始实现中，上述规则将不再适
用。
```

```
注意
如果你使用扩展提供了一个新的构造器，你依旧有责任确保构造过程能够让实例完全初始化。
```

### 方法
```
extension Int {
    func repetitions(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}

//可变实例方法
extension Int {
    mutating func square() {
        self = self * self
    }
}

//下标
extension Int {
    subscript(digitIndex: Int) -> Int {
        var decimalBase = 1
        for _ in 0..<digitIndex {
            decimalBase *= 10
        }
        return (self / decimalBase) % 10
    }
}
746381295[0]
// 返回 5
746381295[1]
// 返回 9
746381295[2]
// 返回 2
746381295[8]
// 返回 7
```

### 嵌套类
```
extension Int {
    enum Kind {
        case Negative, Zero, Positive
    }
    var kind: Kind {
        switch self {
        case 0:
            return .Zero
        case let x where x > 0:
            return .Positive
        default:
            return .Negative
        }
    }
}
```

```
注意
由于已知 number.kind 是 Int.Kind 类型，因此在 switch 语句中，Int.Kind 中的所有成员值都可
以使用简写形式，例如使用 . Negative 而不是 Int.Kind.Negative。
```

## 协议
### 协议语法
```
protocol SomeProtocol {
    // 这里是协议的定义部分
}
```
### 属性要求
协议可以要求遵循协议的类型提供特定名称和类型的实例属性或类型属性。

```
protocol SomeProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
    static var someTypeProperty: Int { get set }
}
```

### 方法要求
协议可以要求遵循协议的类型实现某些指定的实例方法或类方法。

```
protocol SomeProtocol {
    static func someTypeMethod()
    func random() -> Double
    //mutaing方法
    mutating func toggle()
    //构造器方法
    init(someParameter: Int)
}
```

```
注意
实现协议中的 mutating 方法时，若是类类型，则不用写 mutating 关键字。而对于结构体和枚举，则必
须写 mutating 关键字。
```

```
注意
如果类已经被标记为 final，那么不需要在协议构造器的实现中使用 required 修饰符，因为 final 类不能有子类。关于 final 修饰符的更多内容，请参见防止重写。
```

### 构造器要求在类中的实现
```
class SomeClass: SomeProtocol {
    required init(someParameter: Int) {
        // 这里是构造器的实现部分
    }
}
```

```
注意
如果类已经被标记为 final，那么不需要在协议构造器的实现中使用 required 修饰符，因为 final 类
不能有子类。
```

如果一个子类重写了父类的指定构造器，并且该构造器满足了某个协议的要求，那么该构造器的实现需要同时
标注 required 和 override修饰符

```
protocol SomeProtocol {
    init()
}

class SomeSuperClass {
    init() {
        // 这里是构造器的实现部分
    }
}

class SomeSubClass: SomeSuperClass, SomeProtocol {
    // 因为遵循协议，需要加上 required
    // 因为继承自父类，需要加上 override
    required override init() {
        // 这里是构造器的实现部分
    }
}
```

### 可失败构造器要求
遵循协议的类型可以通过可失败构造器（init?）或非可失败构造器（init）来满足协议中定义的可失败构造器要求。协议中定义的非可失败构造器要求可以通过非可失败构造器（init）或隐式解包可失败构造器（init!）来满足。

### 协议作为类型
协议可以像其他普通类型一样使用，使用场景如下：

- 作为函数、方法或构造器中的参数类型或返回值类型
- 作为常量、变量或属性的类型
- 作为数组、字典或其他容器中的元素类型

```
注意
协议是一种类型，因此协议类型的名称应与其他类型（例如 Int，Double，String）的写法相同，使用大
写字母开头的驼峰式写法，例如（FullyNamed 和 RandomNumberGenerator）。
```

### 通过扩展添加协议一致性
```
注意
通过扩展令已有类型遵循并符合协议时，该类型的所有实例也会随之获得协议中定义的各项功能。
```

```
注意
即使满足了协议的所有要求，类型也不会自动遵循协议，必须显式地遵循协议。
```

### 类类型专属协议
你可以在协议的继承列表中，通过添加 class 关键字来限制协议只能被类类型遵循，而结构体或枚举不能遵循该协议。

```
protocol SomeClassOnlyProtocol: class, SomeInheritedProtocol {
    // 这里是类类型专属协议的定义部分
}
```

```
注意
当协议定义的要求需要遵循协议的类型必须是引用语义而非值语义时，应该采用类类型专属协议。
```

### 协议合成
有时候需要同时遵循多个协议，你可以将多个协议采用 SomeProtocol & AnotherProtocol 这样的格式进行组合，称为 协议合成（protocol composition）。

```
func wishHappyBirthday(to celebrator: Named & Aged) {
    print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
}
```

### 检查协议一致性

- is 用来检查实例是否符合某个协议，若符合则返回 true，否则返回 false。
- as? 返回一个可选值，当实例符合某个协议时，返回类型为协议类型的可选值，否则返回 nil。
- as! 将实例强制向下转换到某个协议类型，如果强转失败，会引发运行时错误。

### 可选的协议要求
在协议中使用 optional 关键字作为前缀来定义可选要求。
可选要求用在你需要和 Objective-C 打交道的代码中。协议和可选要求都必须带上@objc属性。

```
@objc protocol CounterDataSource {
    @objc optional func incrementForCount(count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}
```

```
注意
严格来讲，CounterDataSource 协议中的方法和属性都是可选的，因此遵循协议的类可以不实现这些要
求，尽管技术上允许这样做，不过最好不要这样写。
```

### 协议扩展
协议可以通过扩展来为遵循协议的类型提供属性、方法以及下标的实现。通过这种方式，你可以基于协议本身来实现这些功能，而无需在每个遵循协议的类型中都重复同样的实现，也无需使用全局函数。

```
extension RandomNumberGenerator {
    func randomBool() -> Bool {
        return random() > 0.5
    }
}
```

### 为协议扩展添加限制条件
在扩展协议的时候，可以指定一些限制条件，只有遵循协议的类型满足这些限制条件时，才能获得协议扩展提供的默认实现。这些限制条件写在协议名之后，使用 where 子句来描述，正如Where子句中所描述的。

例如，你可以扩展 CollectionType 协议，但是只适用于集合中的元素遵循了 TextRepresentable 协议的情况：

```
extension Collection where Iterator.Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}
```

```
注意
如果多个协议扩展都为同一个协议要求提供了默认实现，而遵循协议的类型又同时满足这些协议扩展的限制条
件，那么将会使用限制条件最多的那个协议扩展提供的默认实现。
```

## 泛型
```
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

```
注意
在上面三个函数中，a 和 b 类型相同。如果 a 和 b 类型不同，那它们俩就不能互换值。Swift 是类型安
全的语言，所以它不允许一个 String 类型的变量和一个 Double 类型的变量互换值。试图这样做将导致
编译错误。
```

### 泛型语法

```
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoValues(&someInt, &anotherInt)
// someInt 现在 107, and anotherInt 现在 3

var someString = "hello"
var anotherString = "world"
swapTwoValues(&someString, &anotherString)
// someString 现在 "world", and anotherString 现在 "hello"
```

```
注意
请始终使用大写字母开头的驼峰命名法（例如 T 和 MyTypeParameter）来为类型参数命名，以表明它们是
占位类型，而不是一个值。
```

### 泛型类型

```
struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}
```

### 扩展一个泛型类型
当你扩展一个泛型类型的时候，你并不需要在扩展的定义中提供类型参数列表。
```
extension Stack {
    var topItem: Element? {
        return items.isEmpty ? nil : items[items.count - 1]
    }
}
```

### 类型约束语法
```
func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
    // 这里是泛型函数的函数体部分
}
```

不是所有的 Swift 类型都可以用等式符（==）进行比较。比如说，如果你创建一个自定义的类或结构体来表示一个复杂的数据模型，那么 Swift 无法猜到对于这个类或结构体而言“相等”意味着什么。正因如此，这部分代码无法保证适用于每个可能的类型 T，当你试图编译这部分代码时会出现相应的错误。

Swift 标准库中定义了一个 Equatable 协议，该协议要求任何遵循该协议的类型必须实现等式符（==）及不等符(!=)，从而能对该类型的任意两个值进行比较。所有的 Swift 标准类型自动支持 Equatable 协议。

任何 Equatable 类型都可以安全地使用在 findIndex(of:in:) 函数中，因为其保证支持等式操作符。


```
func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

### 关联类型
定义一个协议时，有的时候声明一个或多个关联类型作为协议定义的一部分将会非常有用。关联类型为协议中的某个类型提供了一个占位名（或者说别名），其代表的实际类型在协议被采纳时才会被指定。你可以通过 associatedtype 关键字来指定关联类型。

```
protocol Container {
    associatedtype ItemType
    mutating func append(_ item: ItemType)
    var count: Int { get }
    subscript(i: Int) -> ItemType { get }
}
```

### 通过扩展一个存在的类型来指定关联类型
```
extension Array: Container {}
```

### 泛型 Where 语句
你可以通过将 where 关键字紧跟在类型参数列表后面来定义 where 子句，where 子句后跟一个或者多个针对关联类型的约束，以及一个或多个类型参数和关联类型间的相等关系。你可以在函数体或者类型的大括号之前添加 where 子句。

```
func allItemsMatch<C1: Container, C2: Container>
    (_ someContainer: C1, _ anotherContainer: C2) -> Bool
    where C1.ItemType == C2.ItemType, C1.ItemType: Equatable {

        // 检查两个容器含有相同数量的元素
        if someContainer.count != anotherContainer.count {
            return false
        }

        // 检查每一对元素是否相等
        for i in 0..<someContainer.count {
            if someContainer[i] != anotherContainer[i] {
                return false
            }
        }

        // 所有元素都匹配，返回 true
        return true
}
```

### 具有泛型 where 子句的扩展

```
extension Stack where Element: Equatable {
    func isTop(_ item: Element) -> Bool {
        guard let topItem = items.last else {
            return false
        }
        return topItem == item
    }
}
```

## 访问控制
### 模块和源文件
模块指的是独立的代码单元，框架或应用程序会作为一个独立的模块来构建和发布。在 Swift 中，一个模块可以使用 import 关键字导入另外一个模块。

### 访问级别
- `open`和`public`可以访问同一模块源文件中的任何实体，在模块外也可以通过导入该模块来访问源文件里的所有实体。
- `internal`可以访问同一模块源文件中的任何实体，但是不能从模块外访问该模块源文件中的实体。
- `fileprivate`访只能被所定义的文件内部访问。
- `private`只能在所定义的作用域内使用。

`open`为最高访问级别，`private`为最低访问级别。  

`open` > `public` > `internal` > `fileprivate` >  `private`  

`open`只作用于类类型和类的成员，它和`public`的区别如下：

- > `public` 的类，只能在它们定义的模块内部被继承。
- > `public` 的类成员，只能在它们定义的模块内部的子类中重写。
- `open`的类，可以在它们定义的模块中被继承，也可以在引用它们的模块中被继承。
- `open`的类成员，可以在它们定义的模块中子类中重写，也可以在引用它们的模块中的子类重写。
- 把一个类标记为`open`，显式地表明，你认为其他模块中的代码使用此类作为父类，然后你已经设计好了你的类的代码了。

### 访问级别基本原则
- `public`的变量，其类型的访问级别不能是`internal`，`fileprivate`或是`private`的。因为无法保证变量的类型在使用变量的地方也具有访问权限。
- 函数的访问级别不能高于它的参数类型和返回类型的访问级别。因为这样就会出现函数可以在任何地方被访问，但是它的参数类型和返回类型却不可以的情况。

### 默认访问级别
默认为 `internal` 级别。

### 框架的访问级别
当你开发框架时，就需要把一些对外的接口定义为开放访问或公开访问级别，以便使用者导入该框架后可以正常使用其功能。这些被你定义为对外的接口，就是这个框架的 API。

```
注意
框架依然会使用默认的`internal`级别，也可以指定为`fileprivate`或者`private`级别。当你想把某个实体作为
框架的 API 的时候，需显式为其指定`open`或`public`级别。
```

### 自定义类型
如果你将类型指定为`fileprivate`或者`private`级别，那么该类的成员的默认级别也会变成`fileprivate`或者`private`级别。如果你将类指定为`public`或者`internal`，那么该类所有成员的默认级别将是`internal`。


### 元组类型
元组的访问级别将由元组中访问级别最严格的类型来决定

```
注意   
元组的访问级别是在它被使用时自动推断出的，而无法明确指定。
```

### 函数类型
函数的访问级别根据访问级别最严格的参数类型或返回类型的访问级别来决定。

### 枚举类型
枚举成员的访问级别和该枚举类型相同，你不能为枚举成员单独指定不同的访问级别。
枚举定义中的任何原始值或关联值的类型的访问级别至少不能低于枚举类型的访问级别。

### 嵌套类型
如果在 `private` 级别的类型中定义嵌套类型，那么该嵌套类型就自动拥有 `private` 访问级别。如果在 `public` 或者 `internal` 级别的类型中定义嵌套类型，那么该嵌套类型自动拥有 `internal` 访问级别。如果想让嵌套类型拥有 `public` 访问级别，那么需要明确指定该嵌套类型的访问级别。

### 子类
子类的访问级别不得高于父类的访问级别。例如，父类的访问级别是 `internal`，子类的访问级别就不能是 `public`。

### 常量、变量、属性、下标
常量、变量、属性不能拥有比它们的类型更高的访问级别。例如，你不能定义一个 `public` 级别的属性，但是它的类型却是 `private` 级别的。

### Getter 和 Setter
常量、变量、属性、下标的 Getters 和 Setters 的访问级别和它们所属类型的访问级别相同。

```
注意
这个规则同时适用于存储型属性和计算型属性。即使你不明确指定存储型属性的 Getter 和 Setter，
Swift 也会隐式地为其创建 Getter 和 Setter，用于访问该属性的后备存储。使用 
fileprivate(set)，private(set) 和 internal(set) 可以改变 Setter 的访问级别，这对计算型
属性也同样适用。
```

### 构造器
自定义构造器的访问级别可以低于或等于其所属类型的访问级别。唯一的例外是必要构造器，它的访问级别必须和所属类型的访问级别相同。

如同函数或方法的参数，构造器参数的访问级别也不能低于构造器本身的访问级别。

### 默认构造器
如默认构造器所述，Swift 会为结构体和类提供一个默认的无参数的构造器，只要它们为所有存储型属性设置了默认初始值，并且未提供自定义的构造器。

默认构造器的访问级别与所属类型的访问级别相同，除非类型的访问级别是 public。如果一个类型被指定为 public 级别，那么默认构造器的访问级别将为 internal。如果你希望一个 public 级别的类型也能在其他模块中使用这种无参数的默认构造器，你只能自己提供一个 public 访问级别的无参数构造器。

### 结构体默认的成员逐一构造器
如果结构体中任意存储型属性的访问级别为 private，那么该结构体默认的成员逐一构造器的访问级别就是 private。否则，这种构造器的访问级别依然是 internal。

如同前面提到的默认构造器，如果你希望一个 public 级别的结构体也能在其他模块中使用其默认的成员逐一构造器，你依然只能自己提供一个 public 访问级别的成员逐一构造器。

### 协议
协议中的每一个要求都具有和该协议相同的访问级别。你不能将协议中的要求设置为其他访问级别。这样才能确保该协议的所有要求对于任意采纳者都将可用。

```
注意
如果你定义了一个 public 访问级别的协议，那么该协议的所有实现也会是 public 访问级别。这一点不
同于其他类型，例如，当类型是 public 访问级别时，其成员的访问级别却只是 internal。
```

### 协议继承
如果定义了一个继承自其他协议的新协议，那么新协议拥有的访问级别最高也只能和被继承协议的访问级别相同。例如，你不能将继承自 `internal` 协议的新协议定义为 `public` 协议。

### 协议一致性
一个类型可以采纳比自身访问级别低的协议。例如，你可以定义一个 public 级别的类型，它可以在其他模块中使用，同时它也可以采纳一个 internal 级别的协议，但是只能在该协议所在的模块中作为符合该协议的类型使用。

采纳了协议的类型的访问级别取它本身和所采纳协议两者间最低的访问级别。也就是说如果一个类型是 public 级别，采纳的协议是 internal 级别，那么采纳了这个协议后，该类型作为符合协议的类型时，其访问级别也是 internal。

如果你采纳了协议，那么实现了协议的所有要求后，你必须确保这些实现的访问级别不能低于协议的访问级别。例如，一个 public 级别的类型，采纳了 internal 级别的协议，那么协议的实现至少也得是 internal 级别。

```
注意
Swift 和 Objective-C 一样，协议的一致性是全局的，也就是说，在同一程序中，一个类型不可能用两种
不同的方式实现同一个协议。
```

### 扩展
你可以在访问级别允许的情况下对类、结构体、枚举进行扩展。扩展成员具有和原始类型成员一致的访问级别。例如，你扩展了一个 public 或者 internal 类型，扩展中的成员具有默认的 internal 访问级别，和原始类型中的成员一致 。如果你扩展了一个 private 类型，扩展成员则拥有默认的 private 访问级别。

或者，你可以明确指定扩展的访问级别（例如，private extension），从而给该扩展中的所有成员指定一个新的默认访问级别。这个新的默认访问级别仍然可以被单独指定的访问级别所覆盖。

### 通过扩展添加协议一致性

如果你通过扩展来采纳协议，那么你就不能显式指定该扩展的访问级别了。协议拥有相应的访问级别，并会为该扩展中所有协议要求的实现提供默认的访问级别。

### 泛型
泛型类型或泛型函数的访问级别取决于泛型类型或泛型函数本身的访问级别，还需结合类型参数的类型约束的访问级别，根据这些访问级别中的最低访问级别来确定。

### 类型别名
你定义的任何类型别名都会被当作不同的类型，以便于进行访问控制。类型别名的访问级别不可高于其表示的类型的访问级别。例如，private 级别的类型别名可以作为 `private`，`file-private`，`internal`，`public`或者`open`类型的别名，但是 `public` 级别的类型别名只能作为 `public` 类型的别名，不能作为 `internal`，`file-private`，或 `private` 类型的别名。

```
注意
这条规则也适用于为满足协议一致性而将类型别名用于关联类型的情况。
```

## 高级运算符
### 取反`~`
```
let initialBits: UInt8 = 0b00001111
let invertedBits = ~initialBits // 等于 0b11110000
```

### 与运算`&`
```
let firstSixBits: UInt8 = 0b11111100
let lastSixBits: UInt8  = 0b00111111
let middleFourBits = firstSixBits & lastSixBits // 等于 00111100
```

### 或运算`|`
```
let someBits: UInt8 = 0b10110010
let moreBits: UInt8 = 0b01011110
let combinedbits = someBits | moreBits // 等于 11111110
```

### 异或运算`^`
```
let firstBits: UInt8 = 0b00010100
let otherBits: UInt8 = 0b00000101
let outputBits = firstBits ^ otherBits // 等于 00010001
```

### 左移`<<`和右移`>>`
对无符号整数进行移位的规则如下：

- 已经存在的位按指定的位数进行左移和右移。
- 任何因移动而超出整型存储范围的位都会被丢弃。
- 用 0 来填充移位后产生的空白位。

```
let shiftBits: UInt8 = 4 // 即二进制的 00000100
shiftBits << 1           // 00001000
shiftBits << 2           // 00010000
shiftBits << 5           // 10000000
shiftBits << 6           // 00000000
shiftBits >> 2           // 00000001
```

### 溢出运算符
在默认情况下，当向一个整数赋予超过它容量的值时，Swift 默认会报错，而不是生成一个无效的数。这个行为为我们在运算过大或着过小的数的时候提供了额外的安全性。

然而，也可以选择让系统在数值溢出的时候采取截断处理，而非报错。

- 溢出加法 `&+`
- 溢出减法 `&-`
- 溢出乘法 `&*`

### 数值溢出
```
var unsignedOverflow = UInt8.max
// unsignedOverflow 等于 UInt8 所能容纳的最大整数 255
unsignedOverflow = unsignedOverflow &+ 1
// 此时 unsignedOverflow 等于 0

var unsignedOverflow = UInt8.min
// unsignedOverflow 等于 UInt8 所能容纳的最小整数 0
unsignedOverflow = unsignedOverflow &- 1
// 此时 unsignedOverflow 等于 255
```

### 优先级和结合性
```
注意
相对 C 语言和 Objective-C 来说，Swift 的运算符优先级和结合性规则更加简洁和可预测。但是，这也
意味着它们相较于 C 语言及其衍生语言并不是完全一致的。在对现有的代码进行移植的时候，要注意确保运
算符的行为仍然符合你的预期。
```

### 运算符重载
```
struct Vector2D {
    var x = 0.0, y = 0.0
}

extension Vector2D {
    static func + (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y + right.y)
    }
}
```

### 前缀和后缀运算符
当运算符出现在值之前时，它就是前缀的（例如 -a），而当它出现在值之后时，它就是后缀的（例如 b!）。

要实现前缀或者后缀运算符，需要在声明运算符函数的时候在 func 关键字之前指定 prefix 或者 postfix 修饰符：

```
extension Vector2D {
    static prefix func - (vector: Vector2D) -> Vector2D {
        return Vector2D(x: -vector.x, y: -vector.y)
    }
}
```

### 复合赋值运算符
```
extension Vector2D {
    static func += (left: inout Vector2D, right: Vector2D) {
        left = left + right
    }
}
```

```
注意
不能对默认的赋值运算符（=）进行重载。只有组合赋值运算符可以被重载。同样地，也无法对三目条件运算
符 （a ? b : c） 进行重载。
```

### 等价运算符
```
extension Vector2D {
    static func == (left: Vector2D, right: Vector2D) -> Bool {
        return (left.x == right.x) && (left.y == right.y)
    }
    static func != (left: Vector2D, right: Vector2D) -> Bool {
        return !(left == right)
    }
}
```

### 自定义运算符
新的运算符要使用 operator 关键字在全局作用域内进行定义，同时还要指定 prefix、infix 或者 postfix 修饰符：

`prefix operator +++`

```
extension Vector2D {
    static prefix func +++ (vector: inout Vector2D) -> Vector2D {
        vector += vector
        return vector
    }
}
```

### 自定义中缀运算符的优先级
每个自定义中缀运算符都属于某个优先级组。  
而没有明确放入优先级组的自定义中缀运算符会放到一个默认的优先级组内，其优先级高于三元运算符。

此运算符属于 `AdditionPrecedence` 优先组：

```
infix operator +-: AdditionPrecedence
extension Vector2D {
    static func +- (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y - right.y)
    }
}
let firstVector = Vector2D(x: 1.0, y: 2.0)
let secondVector = Vector2D(x: 3.0, y: 4.0)
let plusMinusVector = firstVector +- secondVector
// plusMinusVector 是一个 Vector2D 实例，并且它的值为 (4.0, -2.0)
```
  

```
注意
当定义前缀与后缀运算符的时候，我们并没有指定优先级。然而，如果对同一个值同时使用前缀与后缀运算
符，则后缀运算符会先参与运算。
```