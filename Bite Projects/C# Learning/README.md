# Notes for Learning C#.NET

## Introduction
###  C# vs .NET
- C# is a programming language
- .NET is a framework for building application on Windows and not limited to C# only

### CLR (Common Language Run-time)
IL - intermediate language; indepentent of the computer
CLR - translates IL to native code called JIT (Just-In-Time) compilation

### Architecture of .NET Applications
Application > Assembly > Namspace > Class

### First C# Program
```csharp
using System;

namespace HelloWorld
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Hello World");
		}
  	}
}
```



