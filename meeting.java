public class Solution {
    
    public int maxWeight(Interval[] intervals) {
        
        //First calculate all possible subsets
        List<List<Interval>> subsets = calculateSubsets(intervals);
        
        //Since they are sorted, find the maximum weight. If intervals
        //overlap, do not use the set.
        int maxWeight = 0;
        for(List<Interal> subset: subsets){
            if(subset.size() > 0){
                int currWeight = subset.get(0).weight;
                int currEnd = subset.get(0).end;
                boolean isCandidate = true;
                
                for(int 1 = 0; i < subset.size(); i++){
                    if(subset.get(i).start < currEnd){
                        isCandidate = false;
                        break;
                    } else {
                        currWeight += subset.get(i).weight;
                        currEnd = subset.get(i).end;
                    }
                }
        
                if(isCandidate){
                    maxWeight = Math.max(currWeight, maxWeight);
                }z
            }
        }
        
        return maxWeight;
        
    }
    
    public List<List<Interval>> calculateSubsets(Interval[] intervals){
        List<List<Intervals>> subsets = new ArrayList<List<String>>();
        subsets.add(new ArrayList<Interval>());
        
        Arrays.sort(intervals, new Comparator<Interval>(){
            @Override
            public int compare(Interval i1, Interval i2){
                return i1.end < i2.end;
            }
        });
        
        for(Interval i: intervals){
            List<List<Interval>> temp = new ArrayList<List<String>>();
            for(List<Intervals> s: subsets){
                ArrayList<Interval> n = new ArrayList<Interval>(s);
                s.add(i);
                temp.add(n);
            }
            subsets.addAll(temp);
        }
        
        return subsets;
    }
}