
MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You are a helpful geometry problem data annotator.Let us annotate these problem texts as geometric formal language.'

MATH_CHAT_BETA_PROMPT = '''
We have these predicates and corresponding literal templates:
Predicate    Literal templates
Point Point(A), Point($) 
Line Line(A,B), Line(m), Line($) 
Angle Angle(A,B,C), Angle(A), Angle(1), Angle($) 
Triangle Triangle(A,B,C), Triangle($), Triangle($1,$2,$3) 
Quadrilateral Quadrilateral(A,B,C,D), Quadrilateral(1), Quadrilateral($) 
Parallelogram Parallelogram(A,B,C,D), Parallelogram(1), Parallelogram($) 
Square Square(A,B,C,D), Square(1), Square($) 
Rectangle Rectangle(A,B,C,D), Rectangle(1), Rectangle($) 
Rhombus Rhombus(A,B,C,D), Rhombus(1), Rhombus($) 
Trapezoid Trapezoid(A,B,C,D), Trapezoid(1), Trapezoid($) 
Kite Kite(A,B,C,D), Kite(1), Kite($) 
Polygon Polygon($) 
Pentagon Pentagon(A,B,C,D,E), Pentagon($) 
Hexagon Hexagon(A,B,C,D,E,F), Hexagon($) 
Heptagon Heptagon(A,B,C,D,E,F,G), Heptagon($) 
Octagon Octagon(A,B,C,D,E,F,G,H), Octagon($) 
Circle Circle(A), Circle(1), Circle($) 
Arc Arc(A,B), Arc(A,B,C), Arc($) 
Sector Sector(O,A,B), Sector($) 
Shape Shape($)
RightAngle RightAngle(Angle($)) 
Right Right(Triangle($)) 
Isosceles Isosceles(Polygon($)) 
Equilateral Equilateral(Polygon($)) 
Regular Regular(Polygon($)) 
Red Red(Shape($)) 
Blue Blue(Shape($)) 
Green Green(Shape($)) 
Shaded Shaded(Shape($))
AreaOf AreaOf(A) 
PerimeterOf PerimeterOf(A) 
RadiusOf RadiusOf(A) 
DiameterOf DiameterOf(A) 
CircumferenceOf CircumferenceOf(A) 
AltitudeOf AltitudeOf(A) 
HypotenuseOf HypotenuseOf(A) 
SideOf SideOf(A) 
WidthOf WidthOf(A) 
HeightOf HeightOf(A) 
LegOf LegOf(A) 
BaseOf BaseOf(A) 
MedianOf MedianOf(A) 
IntersectionOf IntersectionOf(A,B) 
MeasureOf MeasureOf(A) 
LengthOf LengthOf(A) 
ScaleFactorOf ScaleFactorOf(A,B)
PointLiesOnLine PointLiesOnLine(Point($),Line($1,$2)) 
PointLiesOnCircle PointLiesOnCircle(Point($),Circle($)) 
Parallel Parallel(Line($),Line($)) 
Perpendicular Perpendicular(Line($),Line($)) 
IntersectAt IntersectAt(Line($),Line($),Line($),Point($)) 
BisectsAngle BisectsAngle(Line($),Angle($)) 
Congruent Congruent(Polygon($),Polygon($)) 
Similar Similar(Polygon($),Polygon($)) 
Tangent Tangent(Line($),Circle($)) 
Secant Secant(Line($),Circle($)) 
CircumscribedTo CircumscribedTo(Shape($),Shape($)) 
InscribedIn InscribedIn(Shape($),Shape($))
IsMidpointOf IsMidpointOf(Point($),Line($)) 
IsCentroidOf IsCentroidOf(Point($),Shape($)) 
IsIncenterOf IsIncenterOf(Point($),Shape($)) 
IsRadiusOf IsRadiusOf(Line($),Circle($)) 
IsDiameterOf IsDiameterOf(Line($),Circle($)) 
IsMidsegmentOf IsMidsegmentOf(Line($),Triangle($)) 
IsChordOf IsChordOf(Line($),Circle($)) 
IsSideOf IsSideOf(Line($),Polygon($)) 
IsHypotenuseOf IsHypotenuseOf(Line($),Triangle($)) 
IsPerpendicularBisectorOf IsPerpendicularBisectorOf(Line($),Triangle($)) 
IsAltitudeOf IsAltitudeOf(Line($),Triangle($)) 
IsMedianOf IsMedianOf(Line($),Quadrilateral($)) 
IsBaseOf IsBaseOf(Line($),Quadrilateral($)) 
IsDiagonalOf IsDiagonalOf(Line($),Quadrilateral($)) 
IsLegOf IsLegOf(Line($),Trapezoid($))
SinOf SinOf(Var) 
CosOf CosOf(Var) 
TanOf TanOf(Var) 
CotOf CotOf(Var) 
HalfOf HalfOf(Var) 
SquareOf SquareOf(Var) 
SqrtOf SqrtOf(Var) 
RatioOf RatioOf(Var), RatioOf(Var1,Var2) 
SumOf SumOf(Var1,Var2,...) 
AverageOf AverageOf(Var1,Var2,...) 
Add Add(Var1,Var2,...) 
Mul Mul(Var1,Var2,...) 
Sub Sub(Var1,Var2,...) 
Div Div(Var1,Var2,...) 
Pow Pow(Var1,Var2) 
Equals Equals(Var1,Var2) 
Find Find(Var)

Please read the following geometry question text and annotate it as formal language composed of predicates.

After annotating text, please re-examine the text with the formal language to ensure it is consistent and correct. If you find any inconsistencies or reconsider your reasoning, feel free to revise your answer.

After your self-consistency, **provide the formal language in the format: "FormalLanguage: [Predicates]". Do not put extra information except for your option after 'FormalLanguage:' ** 

For example:
Question: "In \\odot K, M N = 16 and m \\widehat M N = 98. Find the measure of L N.",

you should answer:    
"FormalLanguage: [
    "Circle(K)",
    "Equals(LengthOf(Line(M,N)),16)",
    "Equals(MeasureOf(Arc(M,N)),98)",
    "Find(LengthOf(Line(L,N)))"
]"

Now, let us annotate formal language of the following question with this approach.


'''