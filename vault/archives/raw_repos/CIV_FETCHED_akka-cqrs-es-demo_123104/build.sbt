name := "akka-cqrs-es-demo-123104"
version := "0.1"
scalaVersion := "2.13.8"
libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-stream" % "2.6.19",
  "com.typesafe.akka" %% "akka-actor-typed" % "2.6.19",
  "com.lightbend.akka" %% "akka-cluster-tools" % "2.6.19",
  "com.typesafe.akka" %% "akka-persistence-cassandra" % "0.34.7"
)