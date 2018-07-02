<?php
/**
 * Created by PhpStorm.
 * User: coffee
 * Date: 2018-1-2
 * Time: 下午3:03
 */

namespace App\Services;


class AlgorithmService
{
    public function k_mean($data, $cat)
    {
        // default category
        $output = array();
        if ($cat == 1) {
            $output[] = array_keys($data);
            return $output;
        }
        $m = count($data);
        if ($m <= $cat) {
            for ($i = 0 ;$i < $cat; $i++) {
                $output[] = array();
            }
            $i = 0;
            foreach ($data as $k=>$v) {
                $output[$i][] = $k;
                $i++;
            }
            return $output;
        }
        $n = count(pos($data));
        // fill missing value
        $vector = $this->_initial_default_matrix($data, $n);
        // initial default point
        $central_point = array();
        for ($i = 0;$i<$cat;$i++) {
            $temp = array();
            foreach ($vector as $v) {
                //$temp[] = $v * $i / ($cat - 1);
                $temp[] = ($v[1] - $v[0]) * lcg_value() + $v[0];
            }
            $central_point[] = $temp;
        }

        // iteration
        while (1) {
            $category_array = array();
            for ($i = 0 ;$i < $cat; $i++) {
                $category_array[] = array();
            }
            foreach ($data as $k=>$v) {
                $min_distance = null;
                $min_index = 0;
                foreach($central_point as $ck => $cv ) {
                    $distance = 0;
                    for ($i=0;$i<$n;$i++) {
                        $distance += pow($v[$i] - $cv[$i],2);
                    }
                    if (is_null($min_distance) || $distance < $min_distance) {
                        $min_index = $ck;
                        $min_distance = $distance;
                    }
                }
                $category_array[$min_index][] = $k;
            }

            // stop condition
            if ($output == $category_array) {
                return $output;
            } else {
                $output = $category_array;
                // update category_array
                $this->update_point($data, $category_array, $central_point);
            }
        }
    }

    private function _initial_default_matrix(&$data, $n) {
        $vector = array();
        for ($j=0;$j<$n;$j++) {
            $row_sum = array();
            $fill_index = [];
            $max = 0;
            $min = null;
            foreach ($data as $k => $v) {
                if(is_null($v[$j])) {
                    $fill_index[] = $k;
                }else{
                    $row_sum[] = $v[$j];
                    if ($v[$j] > $max) $max = $v[$j];
                    if (is_null($min) || $v[$j] < $min) $min = $v[$j];
                }
            }
            $vector[] = [$min,$max];
            // TODO
            $default = array_sum($row_sum)/count($row_sum);
            foreach ($fill_index as $in) {
               $data[$in][$j] = $default;
            }
        }
        return $vector;
    }


    /**
     * @param array $data
     * @param array $keys
     */
    private function update_point(&$data, $keys, &$central_point)
    {
        $n = count(pos($data));
        foreach ($keys as $in => $ks) {
            if (count($ks) == 0) continue;
            $row = array();
            for ($i=0;$i<$n;$i++) {
                $col = array();
                foreach ($ks as $k) {
                    $col[] = $data[$k][$i];
                }
                $col_avg = array_sum($col) / count($col);
                $row[] = $col_avg;
            }
            $central_point[$in] = $row;
        }
    }

}