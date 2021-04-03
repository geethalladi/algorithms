#!/usr/bin/env hy

(require [hy.contrib.walk [let]])
(import [algo.graphs.graph [Graph]])

(+ 1 1)

(let [x 1]
  (print x))

(defn build-graph [name directed &rest e]
  "Helps build a graph"
  (.build Graph
          name
          e
          :directed True))

;; a simple function would work here
;; this could be easily replaced with a smaller function
;; (defmacro build [name directed &rest e]
;;   `(.build Graph
;;            ~name
;;            ~e
;;            :directed ~directed))

(defn build [name directed &rest e]
  (.build Graph name e :directed directed))

;; ideal scenario
;; (build "test-graph" :directed True
;;        '(a b 5) '(b c 10) '(c d 12))

(let [g (build "test-graph" True
               ["a" "b" 5]
               ["a" "c" 10]
               ["b" "e" 20]
               ["b" "c" 15]
               ["c" "d"])]
  (.view g))
