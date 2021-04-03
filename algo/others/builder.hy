#!/usr/bin/env hy

(require [hy.contrib.walk [let]])
(import [algo.graphs.graph [Graph]])

(+ 1 1)

(let [x 1]
  (print x))

(defn build-graph [name]
  "Helps build a graph"
  (.build Graph
          name
          [(, "a" "b" 5)
           (, "a" "c" 10)
           (, "b" "e" 20)
           (, "b" "c" 15)
           (, "c" "d")]
          :directed True))

(let [g (build-graph "test-graph-builder")]
  (.view g))
