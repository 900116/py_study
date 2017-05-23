//: Playground - noun: a place where people can play

import UIKit

//MARK: 基础部分
//十进制：
let d_i = 17
//二进制：
let b_i = 0b00100
//八进制：
let o_i = 0o21
//十六进制: 
let h_i = 0x1a43
//定义新的类型
typealias UID = UInt16
//布尔类型
let b_value:Bool = true
let temp:Int? = 5
let temp2:Int? = nil
//if 不能判断非bool类型，不过可以用绑定
if temp == 3 {
    print("hah_0")
}
//或者
if let x = temp {
    print("hah_1")
}
//必须每个绑定都非nil，if才能为真
if let x = temp,let y = temp2 {
    print("hah_2")
}
//函数抛出异常
func canThrowAnError() throws{
}
//捕获异常
enum DAOError: Error {
    case noData
    case primaryKeyNull
}
do {
    //some code
    try canThrowAnError()
} catch DAOError.noData  {
    
} catch DAOError.primaryKeyNull{
}
//断言
let age = 10
assert(age >= 0)
assert(age >= 0,"年龄不能小于0")






//MARK: 运算符
//swift 可以用>=和<=
1 >= 1
2 <= 1
//?和!
//可空类型
var p_str:String? = "testStr"
//对可空类型进行解包
var f_str:String = p_str!
//可空类型必须解包才能调用属性和方法
let p_str_count = p_str?.characters.count
p_str = nil
//对nil用！解包会造成崩溃(运行时错误)
//let p_str_count2 = p_str!.characters.count
//对nil用? 解包会返回nil，但不会崩溃
let p_str_count3 = p_str?.characters.count
//空合运算符
let a:String? = "hey"
var b = "yes"
b = a ?? b //等价于 a!=nil?a!:b
//区间运算符
//闭区间(包括a和b的值)
for i in 1...5 {
    print(i)  //打印1，2，3，4，5
}
//半开区间(包括a的值，不包括b的值)
for i in 1..<5 {
    print(i)  //打印1，2，3，4，5
}





//MARK: 元组
//组装
let httpError = (404,"Not Found")
//拆解
let (status,msg) = httpError
//默认参数构造器
let httpError2 = (statusCode:200,description:"OK")
//通过参数名访问
let statusCode = httpError2.statusCode
//元组的比较
//元组大小会按照从左到右、逐值比较的方式
(1, "zebra") < (2, "apple")   // true，因为 1 小于 2
(3, "apple") < (3, "bird")    // true，因为 3 等于 3，但是 apple 小于 bird
(4, "dog") == (4, "dog")      // true，因为 4 等于 4，dog 等于 dog





//MARK: 字符串
//String不是NSString String是值类型
var str = "abc"
var str2 = "def"
//字符串可以做加法
var str3 = str + str2
//得到字符个数
str3.characters.count
var str4 = "abc"
//通过==和!=比较值
str == str4
//字符串插值
let interV = 5
var str5 = "abc \(interV)"





//MARK: 数组
//Array不是NSArray Array是值类型
var m_arr = [1,2,3,4,5]
//数组可以做加法
m_arr += [6,7]
//是否为空,等价于m_arr.count==0
m_arr.isEmpty
//用区间批量赋值
m_arr[0...3] = [4,3,2,1]
m_arr
//遍历数组
for (idx,value) in m_arr.enumerated(){
    print("idx:\(idx) value:\(value)")
}
print("\n")





//MARK: 集合
//Set不是NSSet Set是值类型
var aSet:Set = [1,2,3]
var bSet:Set = [3,5,6]
var cSet:Set = [1,2]
//自定义符号^+
infix operator ^+:AdditionPrecedence
//给集合添加扩展
extension Set{
    //重载各种运算符
    static func & (_ value1:Set,_ value2:Set) -> Set{
        return value1.intersection(value2)
    }
    
    static func ^+ (_ value1:Set,_ value2:Set) -> Set{
        return value1.symmetricDifference(value2)
    }
    
    static func + (_ value1:Set,_ value2:Set) -> Set{
        return value1.union(value2)
    }
    
    static func - (_ value1:Set,_ value2:Set) -> Set{
        return value1.subtracting(value2)
    }
}

//交集
aSet.intersection(bSet)
aSet & bSet
//不同并集
aSet.symmetricDifference(bSet)
aSet ^+ bSet
//并集
aSet.union(bSet)
aSet + bSet
//差集
aSet.subtracting(bSet)
aSet - bSet
//是否相等
aSet == bSet
//是否是子集(包含相等情况)
cSet.isSubset(of: aSet)
//是否是父集(包含相等情况)
aSet.isSuperset(of: cSet)
//是否是子集(不包含相等情况)
cSet.isStrictSubset(of: aSet)
cSet.isStrictSubset(of: cSet)
//是否是父集(不包含相等情况)
aSet.isStrictSuperset(of: cSet)
aSet.isStrictSuperset(of: aSet)
//没有交集
bSet.isDisjoint(with: cSet)





//MARK: 字典
//Dictionary不是NSDictionary Dictionary是值类型
var dict = [String:Int]()
//字面量
var dict2 = ["X":2,"Y":3]
dict["A"] = 3
dict["B"] = 4
//遍历字典
for (k,v) in dict{
    print("key:\(k) value:\(v)")
}
print("\n")






// MARK: 控制流
// 匿名for
var i = 0
for _ in 1...100 {
    i += 1
}
i
//stride to
for i in stride(from: 10, to: 0, by: -2) {
    print(i)
}
print("\n")
//stride through
for i in stride(from: 0, through: 10, by: 2) {
    print(i)
}
print("\n")
//repeat-while相当于do-while
i = 10
repeat{
    print(i)
    i -= 1
} while i >= 0
print("\n")
i
//switch
let x = 3
switch x {
//用区间
case 0...4:
    print("hello")
//可以添加多个值
case 5,6,7:
    print("hey")
default:
    print("what")
}
print("\n")
//switch tuple
var tup = (3,10)
switch tup {
case (0,0):
    print("must be (0,0)")
//_表示匹配任意值
case (_,0):
    print("such as (1,0),(2,0),(3,0)")
case (3,_):
    print("such as (3,10),(3,2)")
case (5...7,2...8):
    print("such as (5,2),(6,8),(7,3)")
default:
    print("what")
}
print("\n")
//switch let where
tup = (1,-1)
switch tup {
//绑定值以后，可以进行一些条件判断
case let (x,y) where x == y:
    print("such as (1,1),(2,2)")
case let (x,_) where x > 0:
    print("such as (1,-1),(2,-8)")
default:
    print("other")
}
//switch for continue
let arr_ = [3,4,5,6,7]
for x in arr_ {
    switch x {
    case 5,7:
        continue //控制for循环
    default:
        print(x)
    }
}
let arr_filter = arr_.filter{![5,7].contains($0)}
arr_filter
//fallthrough
var result = 0.0
let intval = 66
switch intval {
case 91...100:
     result += Double(intval-90) * 1
     fallthrough //等同于c语言的switch 会自动贯穿到下一个case
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
//continue/break label
var counts = 0
externLoop : for i in 0...5 {
    for j in 0...6 {
        counts += 1
        if j == 1 && i < 3{
            continue externLoop //可以控制外层循环，类似goto
        }
        if j == 3 {
            break externLoop
        }
    }
}
//0,0   0,1   1,0   1,1   2,0  2,1   3,0  3,1   3,2   3,3
print(counts)
//guard 类似if 如果不满足将自动调用else块
func guard_func(obj:String?){
    //判断obj是否为nil，如果为nil，直接return
    guard let _ = obj else {
        return
    }
    //数值合法，做处理
    print(obj!)
}
guard_func(obj: nil)
guard_func(obj: "hey")
//#available 检测系统是否可用
if #available(iOS 10, macOS 10.1,*) {
    //iOS10的新特性
}





//MARK: 函数
func standard_func(name:String?,age:Int?) -> Bool{
    if let _ = name,let _ = age{
        return true
    }
    return false
}
//无返回值的函数可以省略 -> ReturnType
func void_func(name:String){
    print("No Return Func")
}
//无参数无返回值
func void_void_func(){
    print("No Params No Return Func")
}
//多个返回值
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
//from 外标签 hometown 内标签 _ 忽略标签
//如果有外标签 调用时用外标签，没有外标签，调用时用内标签 如果是忽略标签，调用不需要加任何标签
func greet(person: String, from hometown: String)
    -> String {
        return "Hello \(person)!  Glad you could visit from \(hometown)."
}
greet(person: "Bill", from: "Cupertino")
func someFunction(_ firstParameterName: Int,_ secondParameterName: Int) {
    // 在函数体内，firstParameterName 和 secondParameterName 代表参数中的第一个和第二个参数值
}
someFunction(1,2)
//参数默认值
func default_vaule_func(name:String,greet:String = "Hello"){
    print("\(greet) \(name)")
}
default_vaule_func(name: "张三")
default_vaule_func(name: "李四", greet: "Hi")
//可变参数
func avg_func(_ numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }
    return total / Double(numbers.count)
}
avg_func(1, 2, 3, 4, 5)
//inout 参数
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
//嵌套函数
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int {
        return input + 1
    }
    func stepBackward(input: Int) -> Int {
        return input - 1
    }
    return backward ? stepBackward : stepForward
}
chooseStepFunction(backward: true)(3)
chooseStepFunction(backward: false)(3)






//MARK: 闭包
let arr:[String] = ["Susan","Helen","Jack","Mark","Judy"]
var sorted_arr = arr.sorted (by: { (s1:String, s2:String) -> Bool in
    return s1 > s2
})
//自动推到类型，可以省略参数的类型及其括号
sorted_arr = arr.sorted(by:{
    s1,s2 in return s1 > s2
})
//如果只有一行代码，则可以省略return
sorted_arr = arr.sorted(by: {
    s1,s2 in s1 > s2
})
//用$1,$2,$3...替代参数
sorted_arr = arr.sorted(by: {$0 > $1})
//由于String重载了>符号，该方法与by的参数一样，所以可以直接用>代替闭包
sorted_arr = arr.sorted(by: >)
//添加一个函数
extension String {
    static func morethan(s1:String,s2:String) -> Bool {
        return s1 > s2
    }
}
//用函数名代替闭包
sorted_arr = arr.sorted(by: String.morethan)
//如果闭包作为函数的最后一个参数可以用尾闭包替代
//省略小括号及其标签
sorted_arr = arr.sorted{ $0 > $1 }
//对比一下
//sorted_arr = arr.sorted(by: {$0 > $1})
//逃逸闭包
var c_arr = [() -> Void]()
//如果不在函数内调用闭包参数，则必须声明为@escaping
func test_escape(closure:@escaping () -> Void) {
    c_arr.append(closure)
}
func test_no_escape(closure:() -> Void) {
    closure()
}
class SomeClass {
    var x = 10
    func doSomething() {
        test_escape {
            self.x = 100  //逃逸闭包必须显示用self引用成员
        }
        test_no_escape {
            x = 200 //非逃逸闭包则不必
        }
    }
}
//自动闭包
var customersInLine = ["Susan","Judy","Micheal"]
func serve(customer customerProvider:
    @autoclosure () -> String) { //自动闭包
    print("Now serving \(customerProvider())!")
}
//如果没有任何参数的闭包可以声明为自动闭包，自动闭包可以省略大括号
serve(customer: customersInLine.remove(at: 0))
//其等同于      滥用自动闭包，影响代码可读性
//serve(customer: {customersInLine.remove(at: 0)})
//自动闭包的逃逸需要同时加入两个关键字
var customerProviders: [() -> String] = []
func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
    customerProviders.append(customerProvider)
}
collectCustomerProviders(customersInLine.remove(at: 0))
collectCustomerProviders(customersInLine.remove(at: 0))






//MARK: 枚举
//枚举并不会绑定为int类型，枚举就是独一无二的类型和值,它的原始值就是它本身，除非你设定原始值
enum CompassPoint {
    case north
    case south
    case east
    case west
}
//只要编译器可以推断类型，就可以省略类型名字
var directionToHead = CompassPoint.west
directionToHead = .east
let directionToHead2:CompassPoint = .north
enum Planet {
    case mercury, venus, earth, mars,
    jupiter, saturn, uranus, neptune
}
//必须遍历出枚举所有值，或者用default，否则会编译错误
switch directionToHead2 {
case .north:
    print("N")
case .west:
    print("W")
case .east:
    print("E")
case .south:
    print("S")
}
//关联值
enum GoodsCode {
    //二维码
    case qrCode(String)
    //条形码
    case upc(Int,Int,Int,Int)
}

var code:GoodsCode = .upc(8, 8, 8, 8)
code = .qrCode("ABCDEF")

switch code {
//如果所有的值都被绑定，则let可以提前
case let .upc(a,b,c,d):
    print("\(a),\(b),\(c),\(d)")
case .qrCode(let codeStr):
    print(codeStr)
}
//原始值
//设定了原始值,会按照OC的规则设定枚举值
enum Planet_I: Int {
    case mercury = 1, venus, earth, mars,
    jupiter, saturn, uranus, neptune
}
Planet_I.mercury.rawValue
//可以用原始值来初始化枚举
let t_p = Planet_I(rawValue: 3)
//原始值不存在，返回nil
let t_p2 = Planet_I(rawValue: 12)
//递归枚举
enum MathExp {
    case number(Int)
    //用indirect 表示可以递归
    indirect case add(MathExp, MathExp)
    indirect case mul(MathExp, MathExp)
    indirect case sub(MathExp, MathExp)
    indirect case div(MathExp, MathExp)
}
//也可以在整个枚举类签名加入indirect表示所有枚举值可递归
indirect enum MathExp2 {
    case number(Int)
    case addition(MathExp2, MathExp2)
    case multiplication(MathExp2, MathExp2)
}
/*
 例如，表达式(5 + 4) * 2，乘号右边是一个数字，左边则是另一个表达式。因为数据是嵌套的，因而用来存储数据的枚举类型也需要支持这种嵌套——这意味着枚举类型需要支持递归。
 也就是说5,(5+4),(5+4)*2 均是数学表达式 这个枚举的一个枚举值
*/
//递归计算数学表达式函数
func evalMathExp(_ exp:MathExp) -> Int {
    switch exp {
    case let .number(value):
        return value
    case let .add(left,right):
        return evalMathExp(left) + evalMathExp(right)
    case let .sub(left,right):
        return evalMathExp(left) - evalMathExp(right)
    case let .mul(left,right):
        return evalMathExp(left) * evalMathExp(right)
    case let .div(left,right):
        return evalMathExp(left) / evalMathExp(right)
    }
}
//创建一个表达式
let exp:MathExp = .number(5)
let exp2:MathExp = .number(4)
let addExp:MathExp = .add(exp,exp2)
let mulExp:MathExp = .mul(addExp,.number(2))
evalMathExp(mulExp)





//MARK: 类与结构体
//创建一个结构体，结构体是值类型
struct Resolution {
    var width = 0
    var height = 0
}
struct MoblieModel {
    var resolution = Resolution()
}
var mob = MoblieModel()
//结构体可以直接改变子属性
mob.resolution.height = 10
//自动生成逐一成员构造器
let res = Resolution(width: 10, height: 20)
//创作一个类
class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}
// 等价于 === 与 不等价于 !==
let v1 = VideoMode()
let v2 = VideoMode()
let v3 = v1
v1 === v2  //比较引用
v1 === v3
// == 是否相等依赖于实现
